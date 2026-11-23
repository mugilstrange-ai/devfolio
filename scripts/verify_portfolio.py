from html.parser import HTMLParser
from pathlib import Path
import re

html=Path("index.html").read_text()
css=Path("style.css").read_text()
md=Path("README.md").read_text()
class Inspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags=[]
        self.links=[]
        self.meta=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        self.tags.append((tag,d))
        if tag=="a":
            self.links.append(d.get("href",""))
        if tag=="meta": self.meta.append(d)
parsed=Inspector()
parsed.feed(html)
tags=parsed.tags
assert any(t=="header" for t,_ in tags),"header missing"
assert any(t=="main" for t,_ in tags),"main missing"
assert any(t=="footer" and d.get("id")=="contact" for t,d in tags),"contact footer missing"
assert any(t=="nav" for t,_ in tags),"navigation missing"
assert any(t=="section" and d.get("id")=="about" for t,d in tags),"about section missing"
assert any(t=="section" and d.get("id")=="projects" for t,d in tags),"projects section missing"
assert "<title>" in html and "</title>" in html,"HTML title missing"
assert any(m.get("name")=="viewport" for m in parsed.meta),"viewport meta missing"
assert all(link in parsed.links for link in ["#about","#projects","#contact"]),"navigation anchors missing"
assert len(re.findall(r'<article class="project-card"',html)) >= 2,"need >=2 projects"
assert "display:flex" in css,"Flexbox missing"
assert "display:grid" in css and "grid-template-columns:repeat" in css,"CSS grid missing"
assert "@media(min-width:" in css,"desktop responsive breakpoint missing"
assert "img{max-width:100%;height:auto}" in css,"responsive image rule missing"
assert "mailto:mugilstrange@gmail.com" in parsed.links,"email link missing"
assert "https://github.com/mugilstrange-ai" in parsed.links,"GitHub link missing"
assert any("linkedin.com" in s for s in parsed.links),"LinkedIn link missing"
assert "https://mugilstrange-ai.github.io/devfolio/" in md,"README live URL missing"
assert Path("assets/favicon.svg").exists(),"favicon missing"
print("PASS: 17 semantic, responsive layout, link and README checks")
