"""Printables zoekt op alle woorden; daarom korte varianten. Ook YouTube opnieuw voor een lege term."""
import json,sys
sys.argv=[sys.argv[0]]
exec(open("meet.py").read().split("uit={")[0])
KORT={"split model for 3d printing blender":"split model","ball joint blender addon":"ball joint","articulated figure blender":"articulated figure",
"action figure blender":"action figure","poseable figure 3d print":"poseable figure","split model 3d print":"split","3d print connectors blender":"connector pin",
"cut model into parts blender":"cut model","blender 3d print addon":"blender addon","print in place joints":"print in place joints"}
uit={}
for lang,k in KORT.items():
    p,pt=printables(k); uit[lang]={"printables_kort":k,"printables":p,"printables_totaal":pt}
uit["3d print connectors blender"]["youtube"]=youtube("3d print connectors blender")
json.dump(uit,sys.stdout,indent=1,ensure_ascii=False)
