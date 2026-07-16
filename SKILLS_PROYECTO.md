# Skills de Claude Code para el Observatorio de Arbolado Urbano de Temuco

Skills que ayudan a este proyecto (teledetección + geoespacial + web + investigación +
documentos), con **cómo instalarlas en otra máquina/instancia de Claude Code**.
Se entregan **48 skills** agrupadas en NÚCLEO (imprescindibles) y ÚTILES (fases 2-3 y extras).

> Cada skill es un directorio autocontenido en `~/.claude/skills/<nombre>/` (con `SKILL.md`
> y a veces `references/`). La forma más simple de llevarlas es **copiar esos directorios**.

---

## Cómo instalar (3 métodos)

### Método A — Copiar el ZIP (recomendado, sin depender de internet)
Se entrega `skills_observatorio_temuco.zip` con todas las skills de abajo.
```bash
mkdir -p ~/.claude/skills
unzip skills_observatorio_temuco.zip -d ~/.claude/skills/
ls ~/.claude/skills/
```
Windows (PowerShell):
```powershell
New-Item -ItemType Directory -Force $HOME\.claude\skills
Expand-Archive skills_observatorio_temuco.zip -DestinationPath $HOME\.claude\skills\
```
Claude Code detecta las skills al abrir una sesión nueva.

### Método B — Desde el marketplace de origen (para mantenerlas actualizadas)
En una sesión interactiva de Claude Code:
```
/plugin marketplace add guanyang/antigravity-skills
/plugin marketplace add Jeffallan/claude-skills
/plugin marketplace add wshobson/agents
/plugin install <nombre-del-plugin>
```

### Método C — Plugins de Anthropic (para docx / pdf / pptx / xlsx)
```
/plugin marketplace add anthropics/claude-plugins-official
/plugin install anthropic-skills
```

---

## Skills NÚCLEO (imprescindibles para este proyecto)

| Skill | Para qué en ESTE proyecto | Origen |
|---|---|---|
| **geopandas** | Datos vectoriales: loteos, límite comunal, cruces espaciales (pérdida ∩ loteos) | K-Dense |
| **xarray** | Rasters satelitales / NetCDF (imágenes Landsat/Sentinel) | K-Dense |
| **markitdown** | Transcribir el audio de Daniela, convertir PDFs/DOCX a texto | Propia (Nicolás) |
| **investigacion** | Buscar y descargar papers, datos, leyes (metodología del workspace) | Propia (Nicolás) |
| **writing-plans** | Redactar el plan maestro de las 3 capas | antigravity-skills |
| **test-driven-development** | Escribir los tests antes del código GEE | antigravity-skills |
| **verification-before-completion** | No declarar "listo" sin correr y verificar | antigravity-skills |
| **dispatching-parallel-agents** | Lanzar agentes de investigación en paralelo | antigravity-skills |
| **data-visualization** | Diseño de gráficos y mapas del dashboard | inferen-sh/skills |
| **database-lookup** | Consultar APIs de datos científicos/abiertos | K-Dense |
| **docx** | Generar informes Word | anthropic-skills (plugin) |
| **pandas-pro** | Manejo de tablas (series NDVI/LST, loteos) | Jeffallan/claude-skills |

## Skills ÚTILES (amplían capacidades / fases 2 y 3)

| Skill | Para qué | Origen |
|---|---|---|
| **python-pro** · **python-project-structure** | Estructura y calidad del código | Jeffallan · wshobson |
| **python-performance-optimization** · **python-testing-patterns** | Optimizar rasters grandes / tests | wshobson/agents |
| **systematic-debugging** · **superpowers-systematic-debugging** · **debugging-wizard** | Depurar el pipeline GEE / mapa | antigravity · superpowers · Jeffallan |
| **executing-plans** · **subagent-driven-development** · **planning-with-files** | Ejecutar el plan tarea por tarea | antigravity-skills |
| **github-actions-templates** · **github-actions-docs** | Alertas automáticas (Capa 3) y GitHub Pages | wshobson · Anthropic |
| **playwright-expert** | Scraping de portales sin API (IDE, catastros) | Jeffallan/claude-skills |
| **matplotlib** · **seaborn** · **publication-chart-skill** · **scientific-visualization** | Figuras para informes/paper | K-Dense |
| **scientific-schematics** · **mermaid-diagram** · **infographics** | Diagramas del pipeline / infografías ciudadanas | varias |
| **dask** · **zarr-python** · **polars** | Datos grandes / series largas | K-Dense |
| **scikit-learn** · **shap** | ML para conteo de copas (DeepForest, Capa 2 futura) | K-Dense |
| **arxiv** · **semantic-scholar** · **openalex** · **deep-research** | Búsqueda académica ampliada | K-Dense |
| **pdf** · **pptx** · **xlsx** | Otros formatos de entrega | anthropic-skills (plugin) |
| **deploy** · **commit** · **git-workflow** · **code-review** | Publicar en Pages, versionar, revisar | varias |

---

## Dependencias NO-skill (también necesarias)

Las skills son instrucciones; el trabajo real usa estas herramientas. Instalar en destino:

### Python (3.12+)
```bash
pip install earthengine-api geemap rasterio geopandas numpy pandas matplotlib \
            python-dotenv pytest shapely fiona faster-whisper markitdown
```

### Cuentas / credenciales (gratuitas)
- **Google Earth Engine** — cuenta gratis (uso no comercial): registrarse en
  code.earthengine.google.com y crear un Cloud Project. Luego `earthengine authenticate`.
- **GitHub** — para publicar el sitio (GitHub Pages) y versionar. `gh` CLI autenticado.
- (Opcional) **Copernicus CDSE** — descargar Sentinel-2 vía Sentinel Hub
  (SH_CLIENT_ID / SH_CLIENT_SECRET). Solo si se usa el pipeline de descarga local.
- (Opcional) **USGS M2M** — descargar Landsat directo (gratis, sin tarjeta).

### Binarios
- **pandoc** — generar Word/PDF desde markdown (pandoc.org).
- **ffmpeg** — requerido por faster-whisper para leer el audio.

### MCPs útiles (opcionales, mejoran investigación)
- `arxiv` (gratis), `perplexity` (pago), `playwright` (scraping), `github`, `time`.
  Configurar en `~/.claude/settings.json` o `settings.local.json`.

---

## Skills propias — cómo dejarlas completas

### `investigacion` (requiere un archivo extra, YA INCLUIDO en el paquete)
Su `SKILL.md` remite a la **guía maestra** del workspace, que es donde vive la metodología
real (local-first, APIs gratis, verificación de descargas, etc.). Sin esa guía la skill
queda "coja". Por eso el ZIP incluye:
```
_recursos_investigacion/GUIA_MAESTRA_INVESTIGACION.md
```
En la máquina destino, colocá esa guía en una ruta estable y **ajustá la ruta** que aparece
al inicio de `~/.claude/skills/investigacion/SKILL.md` para que apunte a donde la dejaste
(por defecto busca `C:\Users\nmend\OneDrive\Escritorio\claude\GUIA_MAESTRA_INVESTIGACION.md`).
> Nota: esa guía maestra a su vez menciona guías hijas de OTROS proyectos del workspace
> (Recuperación, VRP Chile, Copernicus, Papers). Esas NO aplican al observatorio y no se
> incluyen; la parte común (la guía maestra) es autosuficiente.

Además usa el **MCP `arxiv`** (gratis) para búsqueda de preprints — ver la sección de MCPs.

### `markitdown` (autocontenida)
Trae sus `references/` y `scripts/`. Envuelve la librería `markitdown` de Microsoft
(`pip install markitdown`) + `ffmpeg` para audio. Funciona tal cual.
