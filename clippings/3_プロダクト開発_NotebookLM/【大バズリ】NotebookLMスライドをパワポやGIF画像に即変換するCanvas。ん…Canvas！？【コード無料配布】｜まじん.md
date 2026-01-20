---
title: "【大バズリ】NotebookLMスライドをパワポやGIF画像に即変換するCanvas。ん…Canvas！？【コード無料配布】｜まじん"
source: "https://note.com/majin_108/n/n21d838108820"
author:
  - "[[まじん]]"
published: 2025-12-13
created: 2025-12-14
description: "こんにちは、まじんです。  昨日Xで投稿したこちらのポストがバズってまして。   これにNotebookLMスライドを渡してみて。https://t.co/yxtJNMViWQ — まじん (@Majin_AppSheet) December 12, 2025  いや……投稿から1日経ってないのに まじん式v4 のいいね/インプの半数超えてるんだが…。  しかもこれ、 Geminiと30分くらいお喋りしてたら完成しました。  今回は、このアプリのソースコードを無料公開したいと思います！  また、どのようにGeminiと対話したのか？ そのバイブコーディングのテクニックについては、"
tags:
  - "notebooklm"
  - "ツール開発"
  - "ai活用"
  - "スライド"
  - "canvas"
later: false
---
![見出し画像](https://assets.st-note.com/production/uploads/images/236142317/rectangle_large_type_2_8b8de9ad64a3e3de3795db14c85f5b45.png?width=1280)

## 【大バズリ】NotebookLMスライドをパワポやGIF画像に即変換するCanvas。ん…Canvas！？【コード無料配布】

[まじん](https://note.com/majin_108)

こんにちは、まじんです。

昨日Xで投稿したこちらのポストがバズってまして。

いや……投稿から1日経ってないのに  
まじん式v4 のいいね/インプの半数超えてるんだが…。

しかもこれ、  
**Geminiと30分くらいお喋りしてたら完成しました。**

今回は、このアプリの **ソースコードを無料公開** したいと思います！

**また、どのようにGeminiと対話したのか？  
**そのバイブコーディングのテクニックについては、  
メンバーシップ限定エリアに記載しますね、さすがに。

![画像](https://assets.st-note.com/img/1765636072-Evz7ZSjOGiM1IWJ5mgNlweA9.png?width=1200)

---

## 【無料公開】自分のGeminiで再現しよう！

Gemini（思考モード）で **Canvasをオン** にして、  
以下のプロンプトを送信してみてください。無料GeminiでもOK。

> **以下のコードをCanvasにそのままプレビューしてください。  
> \---  
> \[ソースコード\]**

### ソースコード（Xで公開したこちら）

```cs
import React, { useState, useEffect, useRef } from 'react';
import { Upload, Download, Loader2, CheckCircle2, X, Film, FileArchive, ScrollText, Settings2, Presentation, Sparkles, FileText, Zap, RefreshCw } from 'lucide-react';

// 外部ライブラリの読み込みヘルパー
const loadScript = (src) => {
  return new Promise((resolve, reject) => {
    if (document.querySelector(\`script[src="${src}"]\`)) {
      resolve();
      return;
    }
    const script = document.createElement('script');
    script.src = src;
    script.onload = resolve;
    script.onerror = reject;
    document.body.appendChild(script);
  });
};

export default function App() {
  const [isDragging, setIsDragging] = useState(false);
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState('idle'); // idle, processing, zipping, complete, error
  const [progress, setProgress] = useState({ current: 0, total: 0, message: '' });
  const [generatedImages, setGeneratedImages] = useState([]);
  const [zipBlob, setZipBlob] = useState(null);
  const [errorMsg, setErrorMsg] = useState('');
  const [librariesLoaded, setLibrariesLoaded] = useState(false);
  
  const [gifStatus, setGifStatus] = useState('idle'); 
  const [longImageStatus, setLongImageStatus] = useState('idle');
  const [pptxStatus, setPptxStatus] = useState('idle');
  
  const [gifInterval, setGifInterval] = useState(1.0); // 秒単位

  const fileInputRef = useRef(null);
  const cancelProcessingRef = useRef(false);

  useEffect(() => {
    const loadLibs = async () => {
      try {
        await loadScript('https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js');
        await loadScript('https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js');
        await loadScript('https://cdnjs.cloudflare.com/ajax/libs/gif.js/0.2.0/gif.js');
        await loadScript('https://cdn.jsdelivr.net/npm/pptxgenjs@3.12.0/dist/pptxgen.bundle.js');
        
        if (window.pdfjsLib) {
          window.pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
        }
        setLibrariesLoaded(true);
      } catch (err) {
        setErrorMsg('ライブラリの読み込みに失敗しました。リロードしてください。');
      }
    };
    loadLibs();
  }, []);

  const handleDragOver = (e) => { e.preventDefault(); setIsDragging(true); };
  const handleDragLeave = (e) => { e.preventDefault(); setIsDragging(false); };
  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const droppedFile = e.dataTransfer.files[0];
      droppedFile.type === 'application/pdf' ? startProcessing(droppedFile) : setErrorMsg('PDFファイルのみ対応しています。');
    }
  };
  const handleFileSelect = (e) => {
    if (e.target.files && e.target.files[0]) startProcessing(e.target.files[0]);
  };

  const startProcessing = async (selectedFile) => {
    if (!librariesLoaded) return;
    setFile(selectedFile);
    setStatus('processing');
    setGeneratedImages([]);
    setZipBlob(null);
    setErrorMsg('');
    setGifStatus('idle');
    setLongImageStatus('idle');
    setPptxStatus('idle');
    setProgress({ current: 0, total: 0, message: 'Analyzing Structure...' });
    cancelProcessingRef.current = false;

    try {
      const arrayBuffer = await selectedFile.arrayBuffer();
      const pdf = await window.pdfjsLib.getDocument(arrayBuffer).promise;
      const totalPages = pdf.numPages;
      setProgress({ current: 0, total: totalPages, message: \`Rendering Slides...\` });

      const images = [];
      const zip = new window.JSZip();
      const folder = zip.folder("images");

      for (let i = 1; i <= totalPages; i++) {
        if (cancelProcessingRef.current) break;
        const page = await pdf.getPage(i);
        const scale = 2.0;
        const viewport = page.getViewport({ scale });
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');
        canvas.height = viewport.height;
        canvas.width = viewport.width;

        await page.render({ canvasContext: context, viewport }).promise;

        const blob = await new Promise(resolve => canvas.toBlob(resolve, 'image/png'));
        const dataUrl = canvas.toDataURL('image/png');
        
        images.push({ id: i, dataUrl, name: \`slide_${String(i).padStart(2, '0')}.png\`, width: viewport.width, height: viewport.height });
        folder.file(\`slide_${String(i).padStart(2, '0')}.png\`, blob);
        setProgress({ current: i, total: totalPages, message: \`${Math.round((i / totalPages) * 100)}% Complete\` });
        await new Promise(r => setTimeout(r, 20));
      }

      if (cancelProcessingRef.current) { setStatus('idle'); setFile(null); return; }

      setGeneratedImages(images);
      setStatus('zipping');
      setProgress(prev => ({ ...prev, message: 'Packaging Assets...' }));
      const content = await zip.generateAsync({ type: "blob" });
      setZipBlob(content);
      setStatus('complete');
    } catch (err) {
      console.error(err);
      setErrorMsg('処理中にエラーが発生しました。ファイルを確認してください。');
      setStatus('error');
    }
  };

  const downloadFile = (blob, filename) => {
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  };

  const handleDownloadZip = () => zipBlob && file && downloadFile(zipBlob, \`${file.name.replace('.pdf', '')}_slides.zip\`);

  const generateGif = async () => {
    if (!window.GIF || generatedImages.length === 0) return;
    setGifStatus('processing');
    try {
      const workerResponse = await fetch('https://cdnjs.cloudflare.com/ajax/libs/gif.js/0.2.0/gif.worker.js');
      const workerBlob = await workerResponse.blob();
      const workerUrl = URL.createObjectURL(workerBlob);
      const gif = new window.GIF({ workers: 2, quality: 10, workerScript: workerUrl, width: generatedImages[0].width, height: generatedImages[0].height });

      for (const imgData of generatedImages) {
        const img = new Image();
        img.src = imgData.dataUrl;
        await new Promise(resolve => { img.complete ? resolve() : img.onload = resolve; });
        gif.addFrame(img, { delay: gifInterval * 1000 });
      }

      gif.on('finished', (blob) => {
        downloadFile(blob, \`${file.name.replace('.pdf', '')}_animation.gif\`);
        setGifStatus('complete');
        URL.revokeObjectURL(workerUrl);
      });
      gif.render();
    } catch (err) { setGifStatus('error'); }
  };

  const generatePptx = async () => {
    if (!window.PptxGenJS || generatedImages.length === 0) return;
    setPptxStatus('processing');
    try {
      const pptx = new window.PptxGenJS();
      const firstImg = generatedImages[0];
      const ratio = firstImg.width / firstImg.height;
      if (Math.abs(ratio - 16/9) < 0.1) pptx.layout = 'LAYOUT_16x9';
      else if (Math.abs(ratio - 4/3) < 0.1) pptx.layout = 'LAYOUT_4x3';
      else { pptx.defineLayout({ name: 'CUSTOM', width: 10, height: 10 / ratio }); pptx.layout = 'CUSTOM'; }

      for (const imgData of generatedImages) {
        const slide = pptx.addSlide();
        slide.addImage({ data: imgData.dataUrl, x: 0, y: 0, w: '100%', h: '100%' });
      }
      await pptx.writeFile({ fileName: \`${file.name.replace('.pdf', '')}.pptx\` });
      setPptxStatus('complete');
    } catch (err) { setPptxStatus('error'); }
  };

  const generateLongImage = async () => {
    if (generatedImages.length === 0) return;
    setLongImageStatus('processing');
    try {
      const maxWidth = Math.max(...generatedImages.map(img => img.width));
      const totalHeight = generatedImages.reduce((sum, img) => sum + img.height, 0);
      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');
      canvas.width = maxWidth;
      canvas.height = totalHeight;
      ctx.fillStyle = '#FFFFFF';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      let currentY = 0;
      
      for (const imgData of generatedImages) {
        const img = new Image();
        img.src = imgData.dataUrl;
        await new Promise(resolve => { img.complete ? resolve() : img.onload = resolve; });
        const x = (maxWidth - imgData.width) / 2;
        ctx.drawImage(img, x, currentY);
        currentY += imgData.height;
      }
      canvas.toBlob((blob) => {
        if (blob) {
          downloadFile(blob, \`${file.name.replace('.pdf', '')}_long.png\`);
          setLongImageStatus('complete');
        } else setLongImageStatus('error');
      }, 'image/png');
    } catch (err) { setLongImageStatus('error'); }
  };
  
  const reset = () => {
    setFile(null);
    setStatus('idle');
    setGifStatus('idle');
    setLongImageStatus('idle');
    setPptxStatus('idle');
    setGeneratedImages([]);
    setZipBlob(null);
    setErrorMsg('');
    setProgress({ current: 0, total: 0, message: '' });
    if (fileInputRef.current) fileInputRef.current.value = '';
  };

  const cancel = () => { cancelProcessingRef.current = true; reset(); };
  const progressPercent = progress.total > 0 ? Math.round((progress.current / progress.total) * 100) : 0;

  return (
    <div className="relative min-h-screen bg-slate-950 text-slate-200 font-sans p-6 flex flex-col items-center justify-center overflow-hidden selection:bg-indigo-500/30 selection:text-indigo-100">
      
      {/* Aurora Background Effects */}
      <div className="fixed inset-0 pointer-events-none">
        <div className="absolute top-[-10%] left-[-10%] w-[50%] h-[50%] bg-indigo-600/20 rounded-full blur-[100px] animate-aurora-1"></div>
        <div className="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] bg-cyan-600/20 rounded-full blur-[100px] animate-aurora-2"></div>
        <div className="absolute top-[40%] left-[40%] w-[30%] h-[30%] bg-fuchsia-600/10 rounded-full blur-[100px] animate-aurora-3"></div>
        <div className="absolute inset-0 opacity-[0.03] bg-[url('https://www.transparenttextures.com/patterns/stardust.png')]"></div>
      </div>

      <div className="w-full max-w-5xl space-y-8 relative z-10">
        
        {/* Header Section (Dynamic) */}
        <div className={\`text-center space-y-6 pt-4 transition-all duration-500 ${status === 'complete' ? 'mb-4' : ''}\`}>
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/5 border border-white/10 shadow-[0_0_15px_rgba(255,255,255,0.05)] mb-2 animate-fade-in-up backdrop-blur-md">
            <Sparkles className="w-3.5 h-3.5 text-cyan-300" />
            <span className="text-[11px] uppercase tracking-[0.2em] font-bold text-cyan-300/90">Optimized for NotebookLM</span>
          </div>
          
          {status !== 'complete' && (
            <>
              <h1 className="text-4xl md:text-6xl font-extrabold tracking-tight text-white leading-tight drop-shadow-2xl animate-fade-in-up" style={{animationDelay: '0.1s'}}>
                静止したスライドを、<br/>
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-300 via-indigo-300 to-fuchsia-300">自在なビジュアルへ。</span>
              </h1>
              <p className="text-slate-400 text-lg md:text-xl max-w-2xl mx-auto font-light leading-relaxed animate-fade-in-up" style={{animationDelay: '0.2s'}}>
                PDFを瞬時に<span className="text-indigo-200 font-medium">高解像度で画像化</span>し、PowerPointやGIFに再構築。<br className="hidden md:block"/>
                並べ替えも、シェアも、あなたの思いのままに。
              </p>
            </>
          )}
        </div>

        {/* Glassmorphism Main Card Container */}
        <div className={\`transition-all duration-500 ${status === 'complete' ? 'max-w-4xl mx-auto' : ''}\`}>
          
          {/* Upload Area */}
          {status === 'idle' && (
            <div className="bg-white/5 backdrop-blur-2xl rounded-[2.5rem] shadow-[0_8px_32px_0_rgba(0,0,0,0.36)] border border-white/10 overflow-hidden relative">
              <div
                onDragOver={handleDragOver}
                onDragLeave={handleDragLeave}
                onDrop={handleDrop}
                className={\`
                  relative p-24 text-center cursor-pointer group transition-all duration-500
                  ${isDragging ? 'bg-indigo-500/10' : 'hover:bg-white/5'}
                \`}
                onClick={() => fileInputRef.current?.click()}
              >
                <input type="file" ref={fileInputRef} className="hidden" accept="application/pdf" onChange={handleFileSelect} />
                <div className={\`absolute inset-6 rounded-[1.5rem] border border-dashed transition-all duration-500 ${isDragging ? 'border-indigo-400/50 bg-indigo-500/5' : 'border-slate-600/50 group-hover:border-slate-500/80'}\`} />
                <div className="relative z-10 flex flex-col items-center gap-8">
                  <div className={\`
                    w-24 h-24 rounded-3xl flex items-center justify-center shadow-2xl transition-all duration-500 border border-white/10
                    ${isDragging ? 'bg-indigo-500 text-white scale-110 rotate-3 shadow-indigo-500/40' : 'bg-slate-800/50 text-cyan-300 group-hover:scale-105 group-hover:bg-slate-800/80'}
                  \`}>
                    <FileText className="w-10 h-10" />
                  </div>
                  <div className="space-y-3">
                    <p className="text-2xl font-bold text-slate-200 group-hover:text-white transition-colors">
                      PDFファイルをここにドロップ
                    </p>
                    <p className="text-sm text-slate-500 group-hover:text-slate-400">
                      または <span className="text-cyan-300 underline decoration-cyan-900 underline-offset-4 group-hover:decoration-cyan-400 transition-all">ファイルを選択</span>
                    </p>
                  </div>
                  {!librariesLoaded && (
                    <div className="inline-flex items-center gap-2 px-4 py-2 bg-black/20 border border-white/5 text-slate-400 text-xs font-medium rounded-full mt-4 backdrop-blur-sm">
                      <Loader2 className="w-3 h-3 animate-spin text-cyan-400" /> System Initializing...
                    </div>
                  )}
                </div>
              </div>
            </div>
          )}

          {/* Processing View */}
          {(status === 'processing' || status === 'zipping') && (
            <div className="bg-white/5 backdrop-blur-2xl rounded-[2.5rem] shadow-[0_8px_32px_0_rgba(0,0,0,0.36)] border border-white/10 overflow-hidden p-24 flex flex-col items-center justify-center min-h-[500px]">
              <div className="relative w-48 h-48 mb-10">
                 <div className="absolute inset-0 bg-indigo-500/20 blur-3xl rounded-full animate-pulse"></div>
                 <svg className="w-full h-full rotate-[-90deg] relative z-10" viewBox="0 0 100 100">
                  <circle className="text-slate-800/50 stroke-current" strokeWidth="2" cx="50" cy="50" r="46" fill="transparent"></circle>
                  <circle 
                    className="text-cyan-400 stroke-current transition-all duration-300 ease-out drop-shadow-[0_0_8px_rgba(34,211,238,0.8)]" 
                    strokeWidth="2" strokeLinecap="round" cx="50" cy="50" r="46" fill="transparent"
                    strokeDasharray={\`${289.02 * (progressPercent / 100)} 289.02\`}
                  ></circle>
                </svg>
                <div className="absolute inset-0 flex flex-col items-center justify-center z-20">
                  <span className="text-5xl font-black text-white tracking-tighter drop-shadow-lg">{progressPercent}%</span>
                </div>
              </div>
              <h3 className="text-2xl font-bold text-white mb-2 tracking-wide animate-pulse">
                {status === 'zipping' ? 'PACKAGING...' : 'CONVERTING SLIDES...'}
              </h3>
              <p className="text-indigo-200/60 font-mono text-sm mb-10">{progress.message}</p>
              <button onClick={cancel} className="text-slate-500 hover:text-white text-xs tracking-widest font-bold px-8 py-3 rounded-full hover:bg-white/10 border border-transparent hover:border-white/10 transition-all backdrop-blur-md">
                CANCEL
              </button>
            </div>
          )}

          {/* Completion View - New Layout */}
          {status === 'complete' && (
            <div className="flex flex-col items-center w-full animate-fade-in-up">
              
              {/* Compact Header Info */}
              <div className="text-center mb-8 w-full">
                 <div className="inline-flex items-center gap-2 px-4 py-2 bg-emerald-500/10 border border-emerald-500/20 rounded-full text-emerald-400 mb-4 backdrop-blur-md">
                   <CheckCircle2 className="w-4 h-4" />
                   <span className="text-sm font-bold tracking-wide">Ready to Download</span>
                 </div>
                 <h2 className="text-2xl md:text-3xl font-bold text-white mb-2 drop-shadow-lg line-clamp-1 px-4">{file?.name}</h2>
                 <div className="flex items-center justify-center gap-4 text-sm text-slate-400 font-mono">
                    <span className="bg-white/5 px-3 py-1 rounded-md border border-white/5">{generatedImages.length} Slides</span>
                    <span className="bg-white/5 px-3 py-1 rounded-md border border-white/5">{(zipBlob?.size / 1024 / 1024).toFixed(1)} MB</span>
                 </div>
              </div>

              {/* Action Grid (Bento Style) */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 w-full">
                  
                  {/* PNG (ZIP) - Priority */}
                  <button onClick={handleDownloadZip} className="group relative col-span-1 md:col-span-2 p-6 bg-slate-800/40 backdrop-blur-xl border border-white/10 rounded-[1.5rem] hover:bg-slate-700/60 hover:border-cyan-500/30 transition-all duration-300 text-left overflow-hidden shadow-lg hover:shadow-cyan-500/20">
                    <div className="absolute top-0 right-0 p-32 bg-cyan-500/10 rounded-full blur-3xl group-hover:bg-cyan-400/20 transition-all duration-500 translate-x-1/2 -translate-y-1/2"></div>
                    <div className="flex items-start justify-between relative z-10">
                      <div className="space-y-1">
                          <div className="flex items-center gap-3 mb-2">
                             <div className="p-2 bg-cyan-500/20 rounded-lg text-cyan-300 border border-cyan-500/20 shadow-[0_0_15px_rgba(6,182,212,0.3)]">
                                <FileArchive className="w-5 h-5" />
                             </div>
                             <span className="text-[10px] font-bold text-cyan-300/80 uppercase tracking-wider border border-cyan-500/20 px-2 py-0.5 rounded-full bg-cyan-500/5">Recommended</span>
                          </div>
                          <h4 className="text-2xl font-bold text-white group-hover:text-cyan-50 transition-colors">PNG Images (ZIP)</h4>
                          <p className="text-sm text-slate-400 group-hover:text-slate-300">全てのページを個別の高解像度画像として一括保存</p>
                      </div>
                      <div className="w-12 h-12 rounded-full bg-white/5 flex items-center justify-center group-hover:bg-cyan-500 group-hover:text-white transition-all shadow-inner border border-white/5">
                          <Download className="w-6 h-6" />
                      </div>
                    </div>
                  </button>

                  {/* PPTX */}
                  <button onClick={generatePptx} disabled={pptxStatus === 'processing'} className="group relative p-6 bg-slate-800/40 backdrop-blur-xl border border-white/10 rounded-[1.5rem] hover:bg-slate-700/60 hover:border-orange-500/30 transition-all duration-300 text-left overflow-hidden shadow-lg hover:shadow-orange-500/20 disabled:opacity-50">
                      <div className="absolute bottom-0 left-0 p-20 bg-orange-500/10 rounded-full blur-3xl group-hover:bg-orange-400/20 transition-all duration-500 -translate-x-1/3 translate-y-1/3"></div>
                      <div className="flex flex-col h-full justify-between relative z-10">
                         <div className="flex justify-between items-start mb-4">
                            <div className="p-2 bg-orange-500/20 rounded-lg text-orange-300 border border-orange-500/20 shadow-[0_0_15px_rgba(249,115,22,0.3)]">
                              {pptxStatus === 'processing' ? <Loader2 className="w-5 h-5 animate-spin" /> : <Presentation className="w-5 h-5" />}
                            </div>
                            {pptxStatus === 'complete' ? 
                              <div className="bg-emerald-500/20 text-emerald-400 p-1.5 rounded-full border border-emerald-500/20"><CheckCircle2 className="w-4 h-4" /></div> 
                              : <div className="bg-white/5 p-1.5 rounded-full group-hover:bg-orange-500/20 group-hover:text-orange-300 transition-colors"><Download className="w-4 h-4 text-slate-500" /></div>
                            }
                         </div>
                         <div>
                            <h4 className="text-lg font-bold text-white mb-0.5 group-hover:text-orange-50 transition-colors">PowerPoint</h4>
                            <p className="text-[11px] text-slate-400">画像貼り付け済みスライド (PPTX)</p>
                         </div>
                      </div>
                  </button>

                  {/* GIF & Long PNG Cell */}
                  <div className="flex flex-col gap-4">
                      {/* GIF */}
                      <div className="group relative p-4 bg-slate-800/40 backdrop-blur-xl border border-white/10 rounded-[1.5rem] hover:bg-slate-700/60 hover:border-fuchsia-500/30 transition-all duration-300 overflow-hidden shadow-lg hover:shadow-fuchsia-500/20 flex items-center justify-between">
                         <div className="flex items-center gap-3 relative z-10">
                            <div className="p-2 bg-fuchsia-500/20 rounded-lg text-fuchsia-300 border border-fuchsia-500/20 shadow-[0_0_15px_rgba(217,70,239,0.3)]">
                               {gifStatus === 'processing' ? <Loader2 className="w-4 h-4 animate-spin" /> : <Film className="w-4 h-4" />}
                            </div>
                            <div>
                               <h4 className="text-sm font-bold text-white group-hover:text-fuchsia-50 transition-colors">GIF Animation</h4>
                               <div className="flex items-center gap-2 mt-0.5">
                                   <select 
                                     value={gifInterval}
                                     onChange={(e) => setGifInterval(Number(e.target.value))}
                                     disabled={gifStatus === 'processing'}
                                     className="text-[10px] bg-black/30 border border-white/10 rounded px-1.5 py-0.5 text-slate-300 focus:outline-none hover:bg-black/50 cursor-pointer"
                                   >
                                      <option value={0.5}>0.5s</option>
                                      <option value={1.0}>1.0s</option>
                                      <option value={2.0}>2.0s</option>
                                   </select>
                               </div>
                            </div>
                         </div>
                         <button onClick={generateGif} disabled={gifStatus === 'processing'} className="relative z-10 text-[10px] font-bold bg-white/5 text-slate-300 border border-white/5 px-4 py-2 rounded-full hover:bg-fuchsia-500 hover:text-white hover:border-fuchsia-400 transition-all shadow-sm">
                            {gifStatus === 'complete' ? 'RETRY' : 'CREATE'}
                         </button>
                      </div>

                      {/* Long PNG */}
                      <button onClick={generateLongImage} disabled={longImageStatus === 'processing'} className="group relative p-4 bg-slate-800/40 backdrop-blur-xl border border-white/10 rounded-[1.5rem] hover:bg-slate-700/60 hover:border-blue-500/30 transition-all duration-300 overflow-hidden shadow-lg hover:shadow-blue-500/20 flex items-center justify-between text-left disabled:opacity-50 flex-1">
                         <div className="flex items-center gap-3 relative z-10">
                            <div className="p-2 bg-blue-500/20 rounded-lg text-blue-300 border border-blue-500/20 shadow-[0_0_15px_rgba(59,130,246,0.3)]">
                               {longImageStatus === 'processing' ? <Loader2 className="w-4 h-4 animate-spin" /> : <ScrollText className="w-4 h-4" />}
                            </div>
                            <div>
                               <h4 className="text-sm font-bold text-white group-hover:text-blue-50 transition-colors">Long PNG</h4>
                               <p className="text-[10px] text-slate-400">縦読みスクロール</p>
                            </div>
                         </div>
                         <div className="relative z-10">
                            {longImageStatus === 'complete' ? 
                              <div className="bg-emerald-500/20 text-emerald-400 p-1 rounded-full"><CheckCircle2 className="w-4 h-4" /></div>
                              : <div className="bg-white/5 p-1.5 rounded-full group-hover:bg-blue-500/20 group-hover:text-blue-300 transition-colors"><Download className="w-4 h-4 text-slate-500" /></div>
                            }
                         </div>
                      </button>
                  </div>

              </div>
              
              <button 
                onClick={reset}
                className="mt-8 text-slate-500 hover:text-white flex items-center gap-2 text-xs font-bold tracking-widest uppercase hover:underline decoration-slate-600 underline-offset-4 transition-colors relative z-10"
              >
                <RefreshCw className="w-3.5 h-3.5" /> Start Over
              </button>

            </div>
          )}

          {/* Error View */}
          {status === 'error' && (
            <div className="bg-white/5 backdrop-blur-2xl rounded-[2.5rem] shadow-[0_8px_32px_0_rgba(0,0,0,0.36)] border border-white/10 overflow-hidden p-20 text-center space-y-6">
              <div className="w-20 h-20 bg-red-900/20 border border-red-500/20 text-red-500 rounded-3xl flex items-center justify-center mx-auto mb-4 shadow-[0_0_30px_rgba(239,68,68,0.1)] backdrop-blur-md">
                <X className="w-10 h-10" />
              </div>
              <h3 className="text-xl font-bold text-slate-200">System Error</h3>
              <p className="text-slate-500 max-w-md mx-auto">{errorMsg}</p>
              <button onClick={reset} className="px-8 py-3 bg-white/10 text-white border border-white/10 rounded-xl hover:bg-white/20 transition-all font-medium shadow-lg backdrop-blur-md">
                RETRY
              </button>
            </div>
          )}
        </div>
        
        {/* Footer info */}
        <div className="flex flex-col items-center justify-center space-y-3 pt-8 pb-4 opacity-40 hover:opacity-100 transition-opacity">
           <div className="flex items-center gap-3 text-[10px] font-bold text-slate-500 tracking-[0.2em] uppercase">
              <div className="flex items-center gap-1">
                 <Zap className="w-3 h-3" />
                 <span>Client-Side Processing</span>
              </div>
              <span className="w-1 h-1 rounded-full bg-slate-600"></span>
              <span>No Uploads</span>
           </div>
           <p className="text-xs font-medium text-slate-600">
             Developed by <span className="text-cyan-600/80">majin</span>
           </p>
        </div>

      </div>
      
      {/* Global Styles for Animations & Aurora */}
      <style>{\`
        @keyframes aurora-1 {
          0%, 100% { transform: translate(0, 0) scale(1); }
          50% { transform: translate(20px, -20px) scale(1.1); }
        }
        @keyframes aurora-2 {
          0%, 100% { transform: translate(0, 0) scale(1); }
          50% { transform: translate(-20px, 10px) scale(1.2); }
        }
        @keyframes aurora-3 {
          0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.3; }
          50% { transform: translate(10px, 10px) scale(0.9); opacity: 0.6; }
        }
        .animate-aurora-1 { animation: aurora-1 10s infinite ease-in-out; }
        .animate-aurora-2 { animation: aurora-2 12s infinite ease-in-out; }
        .animate-aurora-3 { animation: aurora-3 8s infinite ease-in-out; }

        @keyframes fade-in-up {
          from { opacity: 0; transform: translateY(20px); }
          to { opacity: 1; transform: translateY(0); }
        }
        .animate-fade-in-up {
          animation: fade-in-up 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
        }
      \`}</style>
    </div>
  );
}
```

こんな感じでプレビューされたら成功です。  
後は社員やお友達にリンクを共有すればOK！

![画像](https://assets.st-note.com/img/1765628750-9IBlKXjtoDQTmbxPC2OVdMN7.png?width=1200)

---

## 【メンバーシップ限定】バイブコーディングで作ってみよう！

これはバイブコーディングで30分くらいで完成したのですが、  
具体的にどんな指示をGeminiに投げたのか、解説していきます。

**超有益なプロンプトテクニックも紹介しておりますので、**  
気になる方はnoteメンバーシップへの加入をぜひ。

メンバーシップはこちら👇️

[**Majincraft｜まじん** *Google Workspace × Gemini 活用の研究コミュニティ 「Majincraft（マジンクラフト）」。* *note.com*](https://note.com/majin_108/membership)

さて、それでは第一声からいきますよ！

抽選でnoteポイント 最大100%還元 1/14まで

Google Workspace × Gemini 活用の研究コミュニティ 「Majincraft（…[このメンバーシップの詳細](https://note.com/majin_108/membership/join)

PayPay決済で 追加チャンス！ 12/28まで