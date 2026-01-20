import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import fg from "fast-glob";
import matter from "gray-matter";

const SCRIPT_DIR = path.dirname(fileURLToPath(import.meta.url));
const ROOT_DIR = path.resolve(SCRIPT_DIR, "..", "..");
const CLIPPINGS_GLOB = "02_Clippings/**/*.md";
const OUTPUT_PATH = path.join(ROOT_DIR, "00_System", "assets", "index.json");
const EXCERPT_LENGTH = 180;

const toPosixPath = (value) => value.split(path.sep).join("/");

const normalizeTags = (input) => {
  if (!input) return [];
  if (Array.isArray(input)) {
    return Array.from(
      new Set(
        input
          .map((tag) => String(tag).trim())
          .filter((tag) => tag.length > 0)
      )
    );
  }
  if (typeof input === "string") {
    return Array.from(
      new Set(
        input
          .split(/[\s,]+/)
          .map((tag) => tag.trim())
          .filter((tag) => tag.length > 0)
      )
    );
  }
  return [];
};

const stripMarkdown = (markdown) => {
  let text = markdown;
  text = text.replace(/```[\s\S]*?```/g, " ");
  text = text.replace(/~~~[\s\S]*?~~~/g, " ");
  text = text.replace(/`[^`]*`/g, " ");
  text = text.replace(/!\[([^\]]*)\]\([^)]*\)/g, "$1 ");
  text = text.replace(/\[([^\]]+)\]\([^)]*\)/g, "$1 ");
  text = text.replace(/<[^>]+>/g, " ");
  text = text.replace(/^\s*#{1,6}\s+/gm, " ");
  text = text.replace(/^\s*>\s?/gm, " ");
  text = text.replace(/^\s*[-+*]\s+/gm, " ");
  text = text.replace(/^\s*\d+\.\s+/gm, " ");
  text = text.replace(/[\*_~]+/g, " ");
  text = text.replace(/\s+/g, " ").trim();
  return text;
};

const normalizeAdded = (value) => {
  if (!value) return "";
  if (typeof value === "string") return value.trim();
  return String(value).trim();
};

const main = async () => {
  const entries = await fg(CLIPPINGS_GLOB, {
    cwd: ROOT_DIR,
    dot: false,
  });

  const items = [];

  for (const entry of entries) {
    const absolutePath = path.join(ROOT_DIR, entry);
    const raw = await fs.readFile(absolutePath, "utf8");
    const parsed = matter(raw);
    const data = parsed.data ?? {};

    const id = toPosixPath(entry);
    const title = data.title ? String(data.title).trim() : path.basename(entry, ".md");
    const tags = normalizeTags(data.tags);
    const added = normalizeAdded(data.added);
    const author = data.author ? String(data.author).trim() : "";
    const folder = toPosixPath(path.dirname(entry));

    const bodyText = stripMarkdown(parsed.content ?? "");
    const excerpt = bodyText.slice(0, EXCERPT_LENGTH);

    const searchText = [
      title,
      author,
      folder,
      tags.join(" "),
      bodyText,
    ]
      .filter((value) => value && value.length > 0)
      .join(" ")
      .replace(/\s+/g, " ")
      .trim();

    items.push({
      id,
      title,
      tags,
      added,
      author,
      folder,
      excerpt,
      path: id,
      searchText,
    });
  }

  items.sort((a, b) => a.id.localeCompare(b.id));

  const payload = {
    generatedAt: new Date().toISOString(),
    count: items.length,
    items,
  };

  await fs.mkdir(path.dirname(OUTPUT_PATH), { recursive: true });
  await fs.writeFile(OUTPUT_PATH, JSON.stringify(payload, null, 2), "utf8");

  console.log(`index.json generated: ${payload.count} items`);
};

main().catch((error) => {
  console.error("Failed to build index:", error);
  process.exit(1);
});
