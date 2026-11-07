# Vera, 7 nov 2026. Verzamelt add-ons uit de Google Workspace Marketplace via zoekpagina's.
# Elke zoekpagina geeft max 100 kaarten met naam, maker, sterren en gebruikers.
# Gebruik: python3 gwm-zoek-script.py uitvoer.jsonl
import re, sys, json, subprocess, concurrent.futures as cf, html
W = """invoice budget email mail merge pdf form quiz grade class student teacher crm sales lead
contact calendar meeting schedule booking signature sign docusign translate translation ai gpt chatgpt
gemini writing grammar seo chart graph dashboard report export import csv excel json api sync notion
slack jira asana trello hubspot salesforce shopify stripe paypal woocommerce quickbooks xero accounting
finance stock crypto currency tax payroll hr recruit hiring resume attendance timesheet time tracker
task project todo kanban gantt diagram mindmap flowchart drawio image photo icon font emoji color
template theme design slide presentation video audio speech voice transcribe ocr scan barcode qr
label print mailing address map location geocode weather news rss scraper web crawl data clean
duplicate remove merge split sort filter formula regex lookup random generator calculator math
equation latex citation bibliography reference research paper read accessibility dyslexia language
spanish french dictionary thesaurus word count plagiarism essay rubric feedback comment review
approval workflow automation zap trigger schedule reminder notification sms whatsapp telegram
discord twitter linkedin facebook instagram youtube tiktok ads google ads analytics bigquery sql
database firebase supabase airtable mysql postgres backup archive drive folder file share permission
security password encryption audit admin user directory group license signature email tracking open
tracker unsubscribe newsletter campaign marketing survey poll feedback nps event ticket inventory
order product shipping warehouse logistics fleet real estate legal contract law medical health
fitness church school library book reading music game puzzle flashcard vocabulary chemistry physics
biology history geography coding code programming python javascript github markdown html wiki
note notes journal diary planner habit goal okr kpi meeting notes minutes agenda zoom teams webex
phone call dialer support helpdesk ticketing zendesk freshdesk intercom chat chatbot assistant
summary summarize rewrite paraphrase proofread outline brainstorm prompt image generator dalle
midjourney logo watermark compress convert docx pptx xlsx word powerpoint table pivot sparkline
heatmap timeline org chart family tree seating chart roster lottery raffle bingo certificate badge
award report card transcript progress portfolio assignment homework lesson plan curriculum
classroom canvas moodle zoho monday clickup pipedrive mailchimp sendgrid twilio openai claude
anthropic perplexity deepl wordpress webflow wix squarespace figma canva miro lucid
""".split()
def get(q):
    try:
        t = subprocess.run(["curl","-sL","-m","40","https://workspace.google.com/marketplace/search/"+q],capture_output=True,text=True).stdout
    except Exception: return []
    out=[]
    for m in re.finditer(r'href="\./marketplace/app/([a-z0-9_-]+)/(\d+)[^"]*">(.*?)</a>', t, re.S):
        b=m.group(3)
        n=re.search(r'class="M0atNd">(.*?)</div>',b,re.S)
        d=re.search(r'Developer"></span>(.*?)</span>',b,re.S)
        r=re.search(r'Rating">([\d.]+)<',b)
        u=re.search(r'Number of users"></span>([^<]*)<',b)
        out.append(dict(slug=m.group(1),id=m.group(2),naam=html.unescape(n.group(1).strip()) if n else None,
            maker=html.unescape(d.group(1).strip()) if d else None,ster=float(r.group(1)) if r else None,
            gebruikers=u.group(1).strip() if u else None,zoek=q))
    return out
seen={}
with cf.ThreadPoolExecutor(8) as ex:
    for res in ex.map(get, sorted(set(W))):
        for a in res: seen.setdefault(a["id"],a)
with open(sys.argv[1],"w") as f:
    for a in seen.values(): f.write(json.dumps(a,ensure_ascii=False)+"\n")
print(len(seen),"add-ons")
