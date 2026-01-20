const state = {
  items: [],
  itemById: new Map(),
  searchIndex: null,
  tags: [],
  selectedTags: new Set(),
  query: "",
  sort: "relevance",
  repo: null,
};

const elements = {
  searchInput: document.getElementById("searchInput"),
  clearButton: document.getElementById("clearButton"),
  tagList: document.getElementById("tagList"),
  clearTagsBtn: document.getElementById("clearTagsBtn"),
  sortSelect: document.getElementById("sortSelect"),
  resultsList: document.getElementById("resultsList"),
  resultsCount: document.getElementById("resultsCount"),
  metaCount: document.getElementById("metaCount"),
  metaGenerated: document.getElementById("metaGenerated"),
};

const formatGeneratedAt = (value) => {
  if (!value) return "-";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return date.toLocaleString();
};

const escapeHtml = (str) => {
  return String(str)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
};

const highlight = (text, query) => {
  if (!query || !text) return text;
  const escaped = query.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const reg = new RegExp(`(${escaped})`, "gi");
  return String(text).replace(reg, "<mark>$1</mark>");
};

const getAddedValue = (value) => {
  if (!value) return null;
  const parsed = Date.parse(value);
  if (Number.isNaN(parsed)) return null;
  return parsed;
};

const buildSearchIndex = (items) => {
  if (!window.FlexSearch) {
    console.warn("FlexSearch not available, using basic search");
    return null;
  }

  try {
    // FlexSearch 0.7.x の正しい初期化方法
    const index = new window.FlexSearch.Index({
      tokenize: "full",
      cache: 100,
    });

    items.forEach((item) => {
      try {
        index.add(item.id, item.searchText || "");
      } catch (err) {
        console.warn("Failed to add item to index:", item.id, err);
      }
    });

    console.log("Search index built successfully with", items.length, "items");
    return index;
  } catch (error) {
    console.error("Failed to build search index:", error);
    console.warn("Falling back to basic search");
    return null;
  }
};

const normalizeTag = (t) => {
  return String(t || "").trim();
};

const toTagsArray = (tags) => {
  if (Array.isArray(tags)) return tags;
  if (typeof tags === "string" && tags.trim()) {
    // カンマ区切りの文字列も対応
    return tags.split(/[,，\s]+/).map((t) => t.trim()).filter(Boolean);
  }
  return [];
};

const buildTagList = (items) => {
  console.log("buildTagList called with", items?.length, "items");
  const counts = new Map();
  let itemsWithTags = 0;
  
  items.forEach((item) => {
    const tags = toTagsArray(item.tags);
    if (tags.length > 0) {
      itemsWithTags++;
    }
    tags.forEach((raw) => {
      const tag = normalizeTag(raw);
      if (!tag) return;
      counts.set(tag, (counts.get(tag) || 0) + 1);
    });
  });

  console.log("Items with tags:", itemsWithTags, "out of", items.length);
  console.log("Unique tags found:", counts.size);

  const tags = Array.from(counts.entries())
    .map(([name, count]) => ({ name, count }))
    .sort((a, b) => b.count - a.count || a.name.localeCompare(b.name));

  state.tags = tags;
  console.log("buildTagList returning", tags.length, "tags");
  return tags;
};

const renderTags = () => {
  console.log("renderTags called. state.tags.length:", state.tags.length);
  
  const tagListEl = elements.tagList;
  if (!tagListEl) {
    console.error("tagList element not found. Check id=tagList");
    return;
  }
  console.log("tagList element found:", tagListEl);

  tagListEl.innerHTML = "";

  if (state.tags.length === 0) {
    console.warn("No tags to render. state.tags is empty.");
    const empty = document.createElement("div");
    empty.className = "hint";
    empty.textContent = "No tags found";
    tagListEl.appendChild(empty);
    return;
  }

  console.log("Rendering", state.tags.length, "tags");

  const fragment = document.createDocumentFragment();

  state.tags.forEach((tag) => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "tag-chip";
    btn.dataset.tag = tag.name;
    btn.innerHTML = `${escapeHtml(tag.name)} <span class="tag-count">${tag.count}</span>`;

    if (state.selectedTags.has(tag.name)) {
      btn.classList.add("active");
    }

    btn.addEventListener("click", () => {
      if (state.selectedTags.has(tag.name)) {
        state.selectedTags.delete(tag.name);
      } else {
        state.selectedTags.add(tag.name);
      }
      btn.classList.toggle("active");
      renderResults();
    });

    fragment.appendChild(btn);
  });

  tagListEl.appendChild(fragment);
};

const matchesTags = (item) => {
  if (state.selectedTags.size === 0) return true;
  const tags = new Set((item.tags || []).map(normalizeTag));
  // AND: 全選択タグが含まれている必要
  for (const t of state.selectedTags) {
    if (!tags.has(t)) return false;
  }
  return true;
};

const sortItems = (items) => {
  const sortKey = state.sort;
  const query = state.query.trim().toLowerCase();
  
  // Relevanceソート: クエリがある場合は関連度順
  if (sortKey === "relevance" && query) {
    const sorted = [...items];
    sorted.sort((a, b) => {
      const aTitle = (a.title || "").toLowerCase();
      const bTitle = (b.title || "").toLowerCase();
      const aTags = (a.tags || []).join(" ").toLowerCase();
      const bTags = (b.tags || []).join(" ").toLowerCase();
      const aText = (a.searchText || "").toLowerCase();
      const bText = (b.searchText || "").toLowerCase();
      
      // タイトル一致優先
      const aTitleMatch = aTitle.includes(query) ? 1 : 0;
      const bTitleMatch = bTitle.includes(query) ? 1 : 0;
      if (aTitleMatch !== bTitleMatch) return bTitleMatch - aTitleMatch;
      
      // タグ一致優先
      const aTagMatch = aTags.includes(query) ? 1 : 0;
      const bTagMatch = bTags.includes(query) ? 1 : 0;
      if (aTagMatch !== bTagMatch) return bTagMatch - aTagMatch;
      
      // 本文一致
      const aTextMatch = aText.includes(query) ? 1 : 0;
      const bTextMatch = bText.includes(query) ? 1 : 0;
      if (aTextMatch !== bTextMatch) return bTextMatch - aTextMatch;
      
      return 0;
    });
    return sorted;
  }

  const effectiveSort = sortKey === "relevance" ? "added_desc" : sortKey;
  const sorted = [...items];

  if (effectiveSort === "title_asc") {
    sorted.sort((a, b) =>
      a.title.localeCompare(b.title, "en", { numeric: true, sensitivity: "base" })
    );
    return sorted;
  }

  if (effectiveSort === "added_asc") {
    sorted.sort((a, b) => {
      const aValue = getAddedValue(a.added);
      const bValue = getAddedValue(b.added);
      if (aValue === null && bValue === null) return 0;
      if (aValue === null) return 1;
      if (bValue === null) return -1;
      return aValue - bValue;
    });
    return sorted;
  }

  if (effectiveSort === "added_desc") {
    sorted.sort((a, b) => {
      const aValue = getAddedValue(a.added);
      const bValue = getAddedValue(b.added);
      if (aValue === null && bValue === null) return 0;
      if (aValue === null) return 1;
      if (bValue === null) return -1;
      return bValue - aValue;
    });
    return sorted;
  }

  return items;
};

const basicSearch = (items, query) => {
  const lowered = query.toLowerCase();
  return items.filter((item) =>
    (item.searchText || "").toLowerCase().includes(lowered)
  );
};

const renderResults = () => {
  let list = [];
  const query = state.query.trim();

  if (query) {
    if (state.searchIndex) {
      const ids = state.searchIndex.search(query, { limit: state.items.length });
      list = ids
        .map((id) => state.itemById.get(id))
        .filter((item) => item && matchesTags(item));
    } else {
      list = basicSearch(state.items, query).filter(matchesTags);
    }
  } else {
    list = state.items.filter(matchesTags);
  }

  list = sortItems(list);

  elements.resultsCount.textContent = `${list.length}`;
  elements.resultsList.innerHTML = "";

  if (list.length === 0) {
    const empty = document.createElement("div");
    empty.className = "card empty-state";
    empty.textContent = "No results match the current filters.";
    elements.resultsList.appendChild(empty);
    return;
  }

  const fragment = document.createDocumentFragment();

  list.forEach((item, index) => {
    const card = document.createElement("article");
    card.className = "result-card card";
    card.style.setProperty("--delay", `${Math.min(index * 20, 200)}ms`);

    const title = document.createElement("h3");
    title.className = "result-title";
    title.innerHTML = highlight(item.title || "Untitled", query);

    const tags = document.createElement("div");
    tags.className = "tags";
    (item.tags || []).forEach((tag) => {
      const tagSpan = document.createElement("span");
      tagSpan.className = "tag";
      tagSpan.textContent = tag;
      tags.appendChild(tagSpan);
    });

    const meta = document.createElement("div");
    meta.className = "result-meta";

    const added = document.createElement("span");
    added.innerHTML = `<strong>Added</strong> ${item.added ? item.added : "-"}`;

    const author = document.createElement("span");
    author.innerHTML = `<strong>Author</strong> ${item.author || "-"}`;

    const folder = document.createElement("span");
    folder.innerHTML = `<strong>Folder</strong> ${item.folder || "-"}`;

    meta.appendChild(added);
    meta.appendChild(document.createTextNode(" | "));
    meta.appendChild(author);
    meta.appendChild(document.createTextNode(" | "));
    meta.appendChild(folder);

    const excerpt = document.createElement("p");
    excerpt.className = "excerpt";
    excerpt.innerHTML = highlight(item.excerpt || "", query);

    // Openリンク: item.url優先、無ければraw.githubusercontent.com
    let openUrl = "";
    if (item.url && item.url.trim()) {
      openUrl = item.url.trim();
    } else if (state.repo && state.repo.owner && state.repo.repo && state.repo.branch) {
      // raw.githubusercontent.com のURLを構築
      openUrl = `https://raw.githubusercontent.com/${state.repo.owner}/${state.repo.repo}/${state.repo.branch}/${encodeURIComponent(item.path || item.id)}`;
    } else {
      // フォールバック（通常は発生しない）
      openUrl = "#";
    }
    
    const openButton = document.createElement("a");
    openButton.className = "open-button";
    openButton.href = openUrl;
    openButton.target = "_blank";
    openButton.rel = "noopener noreferrer";
    openButton.textContent = "Open";

    card.appendChild(title);
    card.appendChild(tags);
    card.appendChild(meta);
    card.appendChild(excerpt);
    card.appendChild(openButton);

    fragment.appendChild(card);
  });

  elements.resultsList.appendChild(fragment);
};

const attachEvents = () => {
  let debounceTimer = null;

  elements.searchInput.addEventListener("input", () => {
    window.clearTimeout(debounceTimer);
    debounceTimer = window.setTimeout(() => {
      state.query = elements.searchInput.value.trim();
      renderResults();
    }, 180);
  });

  elements.sortSelect.addEventListener("change", () => {
    state.sort = elements.sortSelect.value;
    renderResults();
  });

  elements.clearButton.addEventListener("click", () => {
    elements.searchInput.value = "";
    state.query = "";
    state.selectedTags.clear();
    state.sort = "relevance";
    elements.sortSelect.value = "relevance";
    renderTags();
    renderResults();
  });

  // タグクリアボタン
  if (elements.clearTagsBtn) {
    elements.clearTagsBtn.addEventListener("click", () => {
      state.selectedTags.clear();
      elements.tagList
        .querySelectorAll(".tag-chip.active")
        .forEach((x) => x.classList.remove("active"));
      renderResults();
    });
  }

  // キーボードショートカット
  document.addEventListener("keydown", (e) => {
    // `/`で検索欄にフォーカス（入力中は無視）
    if (e.key === "/" && e.target.tagName !== "INPUT" && e.target.tagName !== "TEXTAREA") {
      e.preventDefault();
      elements.searchInput.focus();
    }
    // `Esc`で検索クリア
    if (e.key === "Escape" && document.activeElement === elements.searchInput) {
      elements.searchInput.value = "";
      state.query = "";
      state.selectedTags.clear();
      state.sort = "relevance";
      elements.sortSelect.value = "relevance";
      renderTags();
      renderResults();
      elements.searchInput.blur();
    }
  });
};

const init = async () => {
  try {
    const indexPath = "./assets/index.json";
    console.log("Attempting to load index.json from:", indexPath);
    
    const response = await fetch(indexPath, { cache: "no-store" });
    console.log("Response status:", response.status, response.statusText);
    
    if (!response.ok) {
      const errorText = await response.text().catch(() => "");
      throw new Error(
        `Failed to load index.json: ${response.status} ${response.statusText}\n` +
        `URL: ${indexPath}\n` +
        `Response: ${errorText.slice(0, 200)}`
      );
    }
    
    const data = await response.json();
    console.log("Index loaded successfully. Items count:", data.count);

    if (!data || !Array.isArray(data.items)) {
      throw new Error("Invalid index.json format: items array not found");
    }

    state.items = data.items;
    state.itemById = new Map(state.items.map((item) => [item.id, item]));
    state.searchIndex = buildSearchIndex(state.items);
    state.repo = data.repo || null;

    elements.metaCount.textContent = String(data.count ?? state.items.length ?? 0);
    elements.metaGenerated.textContent = formatGeneratedAt(data.generatedAt);

    // 診断ログ
    console.log("=== Index loaded successfully ===");
    console.log("items length:", state.items?.length);
    console.log("First item sample:", state.items[0]);
    
    const tagCounts = buildTagList(state.items || []);
    console.log("unique tags:", tagCounts.length);
    console.log("top10 tags:", tagCounts.slice(0, 10));
    console.log("state.tags after buildTagList:", state.tags.length);

    console.log("Calling renderTags()...");
    renderTags();
    console.log("renderTags() completed");
    
    renderResults();
  } catch (error) {
    console.error("Error loading index:", error);
    
    elements.resultsList.innerHTML = "";
    const failure = document.createElement("div");
    failure.className = "card empty-state";
    failure.style.padding = "24px";
    failure.style.textAlign = "center";
    
    const errorTitle = document.createElement("div");
    errorTitle.style.fontWeight = "600";
    errorTitle.style.marginBottom = "12px";
    errorTitle.textContent = "Failed to load search index.";
    failure.appendChild(errorTitle);
    
    const errorDetails = document.createElement("div");
    errorDetails.style.fontSize = "13px";
    errorDetails.style.color = "var(--muted)";
    errorDetails.style.marginTop = "8px";
    errorDetails.textContent = error.message || String(error);
    failure.appendChild(errorDetails);
    
    const helpText = document.createElement("div");
    helpText.style.fontSize = "12px";
    helpText.style.color = "var(--muted)";
    helpText.style.marginTop = "16px";
    helpText.textContent = "Please check the browser console for more details.";
    failure.appendChild(helpText);
    
    elements.resultsList.appendChild(failure);
    
    // タグリストにもエラー表示
    if (elements.tagList) {
      elements.tagList.innerHTML = "";
      const tagError = document.createElement("div");
      tagError.className = "hint";
      tagError.textContent = "Tags unavailable (index not loaded)";
      elements.tagList.appendChild(tagError);
    }
  }
};

attachEvents();
init();
