# Notion Marketplace: sitemap met templates, engelse adressen, steekproef van 240 op prijs
curl -s https://sitemaps.notion.com/sitemap-templates.xml -o st.xml
grep -o '<loc>[^<]*' st.xml | sed 's/<loc>//' | grep -v '/[a-z][a-z]-[a-z][a-z]/\|/[a-z][a-z]/templates' > tu.txt
python3 -c "import random;l=open('tu.txt').read().split();random.seed(7);open('s.txt','w').write('\n'.join(random.sample(l,240)))"
cat s.txt | xargs -P 8 -I{} sh -c 'curl -sL --max-time 25 "{}" | grep -o "\"price\":[0-9.]*" | head -1 | sed "s#^#{} #"' > pr.txt
