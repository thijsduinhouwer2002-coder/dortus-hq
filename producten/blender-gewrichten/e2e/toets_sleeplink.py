# Toets voor de sleeplink van extensions.blender.org (#380, Bram 28 nov 2026).
# Doet na wat Blender doet als je de link in het venster sleept (bl_pkg, EXTENSIONS_OT_package_install
# via _invoke_for_drop en _draw_override_after_sync), zonder het dialoogvenster:
# link ontleden, bron uit ?repository= vinden, bron bijwerken, pakket zoeken op archive_url, installeren.
# Let op: Blender zoekt de link op in de HUIDIGE lijst van het platform. Een link naar een oudere
# versie geeft "not found in the remote repository". Daarom wisselt de link bij elke gratis versie.
# Draaien (heeft internet nodig, dus niet in de gewone e2e):
#   d=$(mktemp -d); BLENDER_USER_RESOURCES=$d BLENDER_USER_CONFIG=$d/config BLENDER_USER_EXTENSIONS=$d/ext \
#   blender -b --factory-startup --online-mode --python e2e/toets_sleeplink.py -- "<link>" ["<link>" ...]
# Uitslag per link: "LINK ... gevonden: click_joints <versie>" en "INSTALL click_joints aan: True".
import bpy, sys, addon_utils
from bl_pkg import bl_extension_ops as ops
from bl_pkg.bl_extension_utils import url_parse_for_blender
links = sys.argv[sys.argv.index("--")+1:]
print("online:", bpy.app.online_access)
for i, r in enumerate(bpy.context.preferences.extensions.repos):
    print("bron", i, r.name, r.remote_url, "aan" if r.enabled else "uit")
bpy.ops.extensions.repo_sync_all()
for link in links:
    url, p = url_parse_for_blender(ops.url_normalize(link))
    repo, idx = ops._preferences_repo_find_by_remote_url(bpy.context, p.get("repository", ""))
    ri, rname, pkg, remote, local = ops.extension_url_find_repo_index_and_pkg_id(url)
    print("LINK", url.rsplit("/", 1)[-1], "| bron uit link:", repo.name if repo else None,
          "| gevonden:", pkg or "NIET GEVONDEN", (remote.version if remote else ""))
    if pkg and not local:
        bpy.ops.extensions.package_install(repo_index=ri, pkg_id=pkg, enable_on_install=True)
        print("INSTALL", pkg, "aan:", any(m.__name__.endswith("." + pkg) for m in addon_utils.modules() if addon_utils.check(m.__name__)[1]))
        print("bron blijft aan voor updates:", bpy.context.preferences.extensions.repos[ri].enabled,
              "| zoekt updates bij start:", bpy.context.preferences.extensions.repos[ri].use_sync_on_startup)
