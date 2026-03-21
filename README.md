# alloyfyi

[![PyPI version](https://agentgif.com/badge/pypi/alloyfyi/version.svg)](https://pypi.org/project/alloyfyi/)
[![Python](https://img.shields.io/pypi/pyversions/alloyfyi)](https://pypi.org/project/alloyfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://pypi.org/project/alloyfyi/)

Python API client and CLI for metal alloys, compositions, and mechanical properties. Access 765 alloys across 12 families — including stainless steels, aluminum alloys, titanium grades, nickel superalloys, and high-entropy alloys — with tensile strength, yield strength, density, hardness, and application data. Zero dependencies.

Extracted from [AlloyFYI](https://alloyfyi.com/), a metallurgy reference platform with 49 glossary terms, 72 educational guides, and comparison tools for engineers, materials scientists, and developers working with metal alloy selection and specification.

> **Explore alloys at [alloyfyi.com](https://alloyfyi.com/)** — browse the [alloy database](https://alloyfyi.com/alloys/), compare [alloy families](https://alloyfyi.com/families/), and read the [metallurgy glossary](https://alloyfyi.com/glossary/).

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/alloyfyi/main/demo.gif" alt="alloyfyi demo — metal alloy lookup, property comparison, and family browsing in Python" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You Can Do](#what-you-can-do)
  - [Alloy Families & Classification](#alloy-families--classification)
  - [Mechanical Properties](#mechanical-properties)
  - [Industrial Applications](#industrial-applications)
  - [Alloy Comparisons](#alloy-comparisons)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [API Reference](#api-reference)
- [Learn More About Alloys](#learn-more-about-alloys)
- [Also Available](#also-available)
- [Science FYI Family](#science-fyi-family)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

## Install

```bash
pip install alloyfyi                # Core (zero deps)
pip install "alloyfyi[cli]"         # + Command-line interface (typer, rich)
pip install "alloyfyi[mcp]"         # + MCP server for AI assistants
pip install "alloyfyi[api]"         # + HTTP client for alloyfyi.com API
pip install "alloyfyi[all]"         # Everything
```

Or run instantly without installing:

```bash
uvx --from alloyfyi alloyfyi search stainless
```

## Quick Start

```python
from alloyfyi.api import AlloyFYI

with AlloyFYI() as api:
    # Browse 765 alloys across 12 families
    alloys = api.list_alloys(limit=10)
    print(alloys["count"])  # 765 total alloys

    # Explore alloy families — steel, aluminum, titanium, nickel, copper
    families = api.list_families()
    for family in families["results"]:
        print(family["slug"])

    # Search for specific alloy types or compositions
    results = api.search("stainless steel")
    print(results["count"])
```

## What You Can Do

### Alloy Families & Classification

Metal alloys are classified into **12 families** based on their base metal and processing characteristics. Each family serves distinct engineering roles determined by mechanical properties, corrosion resistance, and cost.

| Family | Description | Typical Use |
|--------|-------------|-------------|
| **Stainless Steel** | Fe-Cr alloys (>10.5% Cr) with corrosion resistance | Medical instruments, food processing, architecture |
| **Carbon Steel** | Fe-C alloys (0.05-2.0% C), most produced metal | Construction, automotive frames, pipelines |
| **Alloy Steel** | Fe + Cr, Mo, V, Ni for enhanced properties | Gears, shafts, pressure vessels |
| **Tool Steel** | High-hardness Fe alloys (W, Mo, V, Co) | Cutting tools, dies, molds |
| **Structural Steel** | Low-carbon steel for construction loads | Bridges, buildings, infrastructure |
| **Spring Steel** | High yield strength, elastic deformation | Automotive springs, industrial mechanisms |
| **Bearing Steel** | High-carbon chromium steel, fatigue resistant | Ball bearings, roller bearings |
| **Aluminum Alloy** | Al-base with Cu, Mg, Si, Zn additions | Aerospace, automotive, packaging |
| **Titanium Alloy** | Ti-base with Al, V, Mo for strength-to-weight | Aerospace, biomedical implants, marine |
| **Nickel Alloy** | Ni-base superalloys for extreme temperatures | Jet engines, gas turbines, chemical processing |
| **Copper Alloy** | Cu-base (brass, bronze, cupronickel) | Electrical wiring, plumbing, marine hardware |
| **High-Entropy Alloy** | 5+ principal elements in near-equal proportions | Research, next-generation aerospace, nuclear |

```python
from alloyfyi.api import AlloyFYI

with AlloyFYI() as api:
    # List all 12 alloy families
    families = api.list_families()
    for f in families["results"]:
        print(f["slug"])  # stainless-steel, carbon-steel, aluminum-alloy, ...

    # Get family details with member alloys
    stainless = api.get_family("stainless-steel")
    print(stainless)
```

Learn more: [Alloy Families](https://alloyfyi.com/families/) · [Metallurgy Glossary](https://alloyfyi.com/glossary/) · [Alloy Guides](https://alloyfyi.com/guides/)

### Mechanical Properties

Each alloy in the database includes key mechanical and physical properties used in engineering material selection. Properties follow international testing standards (ASTM, ISO).

| Property | Unit | What It Measures |
|----------|------|------------------|
| **Tensile Strength** | MPa | Maximum stress before fracture |
| **Yield Strength** | MPa | Stress at onset of plastic deformation |
| **Density** | g/cm3 | Mass per unit volume |
| **Hardness (Brinell)** | HB | Resistance to indentation |
| **Melting Point** | C | Solid-to-liquid transition temperature |

Additionally, each alloy carries **6-point rating scores** (1-10) for quick comparison:

| Rating | Meaning |
|--------|---------|
| **Strength** | Overall mechanical strength |
| **Corrosion** | Resistance to oxidation and chemical attack |
| **Weight** | Inverse of density (higher = lighter) |
| **Machinability** | Ease of cutting, drilling, and forming |
| **Cost** | Economic value (higher = more affordable) |
| **Temperature** | Performance at elevated temperatures |

```python
from alloyfyi.api import AlloyFYI

with AlloyFYI() as api:
    # Access mechanical properties for any of 765 alloys
    alloy = api.list_alloys(limit=1)
    detail = alloy["results"][0]
    print(detail.get("yield_strength_mpa"))   # e.g., 770.0
    print(detail.get("density_g_cm3"))        # e.g., 6.400
    print(detail.get("rating_strength"))      # e.g., 5
    print(detail.get("rating_corrosion"))     # e.g., 5
```

Learn more: [Alloy Database](https://alloyfyi.com/alloys/) · [Alloy Guides](https://alloyfyi.com/guides/)

### Industrial Applications

AlloyFYI catalogs **30 industrial applications** linking alloy families to real-world engineering use cases — from aerospace turbine blades to surgical implants. Each application describes requirements, common alloy choices, and performance criteria.

```python
from alloyfyi.api import AlloyFYI

with AlloyFYI() as api:
    # Browse 30 application areas
    apps = api.list_applications()
    for app in apps["results"]:
        print(app["slug"])

    # Get application detail with recommended alloys
    detail = api.get_application("aerospace")
```

Learn more: [Applications](https://alloyfyi.com/applications/) · [Metallurgy Glossary](https://alloyfyi.com/glossary/)

### Alloy Comparisons

Compare two alloys side-by-side across all mechanical properties and rating scores. Pre-computed comparisons highlight the differences in strength, weight, corrosion resistance, and cost for common alloy pairs.

```python
from alloyfyi.api import AlloyFYI

with AlloyFYI() as api:
    # Browse pre-computed alloy comparisons
    comparisons = api.list_comparisons(limit=5)
    for comp in comparisons["results"]:
        print(comp["slug"])
```

Learn more: [Alloy Comparisons](https://alloyfyi.com/comparisons/) · [Alloy Guides](https://alloyfyi.com/guides/)

## Command-Line Interface

```bash
pip install "alloyfyi[cli]"

alloyfyi search stainless            # Search alloys, families, applications
alloyfyi search "titanium grade 5"   # Search by grade name
alloyfyi search aerospace            # Search applications
```

## MCP Server (Claude, Cursor, Windsurf)

Add alloy lookup tools to any AI assistant that supports [Model Context Protocol](https://modelcontextprotocol.io/).

```bash
pip install "alloyfyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "alloyfyi": {
            "command": "uvx",
            "args": ["--from", "alloyfyi[mcp]", "python", "-m", "alloyfyi.mcp_server"]
        }
    }
}
```

## REST API Client

```bash
pip install "alloyfyi[api]"
```

```python
from alloyfyi.api import AlloyFYI

with AlloyFYI() as api:
    alloys = api.list_alloys()             # GET /api/v1/alloys/
    families = api.list_families()         # GET /api/v1/families/
    apps = api.list_applications()         # GET /api/v1/applications/
    comparisons = api.list_comparisons()   # GET /api/v1/comparisons/
    results = api.search("titanium")       # GET /api/v1/search/?q=titanium
```

### Example

```bash
curl -s "https://alloyfyi.com/api/v1/families/" | python3 -m json.tool
```

```json
{
  "count": 12,
  "results": [
    {"slug": "stainless-steel"},
    {"slug": "carbon-steel"},
    {"slug": "aluminum-alloy"},
    {"slug": "titanium-alloy"},
    {"slug": "nickel-alloy"},
    {"slug": "copper-alloy"},
    {"slug": "high-entropy-alloy"}
  ]
}
```

Full API documentation at [alloyfyi.com/developers/](https://alloyfyi.com/developers/).

## API Reference

| Method | Description |
|--------|-------------|
| `list_alloys(**params)` | List all 765 alloys with pagination |
| `get_alloy(slug)` | Get alloy detail with properties and ratings |
| `list_families(**params)` | List all 12 alloy families |
| `get_family(slug)` | Get family detail with member alloys |
| `list_applications(**params)` | List 30 industrial applications |
| `get_application(slug)` | Get application detail |
| `list_alloy_applications(**params)` | List alloy-application links |
| `get_alloy_application(slug)` | Get alloy-application detail |
| `list_comparisons(**params)` | List alloy comparisons |
| `get_comparison(slug)` | Get side-by-side comparison |
| `list_glossary(**params)` | List 49 metallurgy glossary terms |
| `get_term(slug)` | Get glossary term definition |
| `list_guides(**params)` | List 72 educational guides |
| `get_guide(slug)` | Get guide content |
| `search(query)` | Search across all alloy content |

## Learn More About Alloys

- **Browse**: [Alloy Database](https://alloyfyi.com/alloys/) · [Alloy Families](https://alloyfyi.com/families/) · [Applications](https://alloyfyi.com/applications/)
- **Compare**: [Alloy Comparisons](https://alloyfyi.com/comparisons/)
- **Reference**: [Metallurgy Glossary](https://alloyfyi.com/glossary/)
- **Guides**: [Educational Guides](https://alloyfyi.com/guides/)
- **API**: [REST API Docs](https://alloyfyi.com/developers/) · [OpenAPI Spec](https://alloyfyi.com/api/v1/)

## Also Available

| Platform | Install | Link |
|----------|---------|------|
| **npm** | `npm install alloyfyi` | [npm](https://www.npmjs.com/package/alloyfyi) |
| **MCP** | `uvx --from "alloyfyi[mcp]" python -m alloyfyi.mcp_server` | [Config](#mcp-server-claude-cursor-windsurf) |

## Science FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem — physical sciences, chemistry, geology, astronomy, and materials.

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| chemfyi | [PyPI](https://pypi.org/project/chemfyi/) | [npm](https://www.npmjs.com/package/chemfyi) | Periodic table, 500 compounds, 371 reactions — [chemfyi.com](https://chemfyi.com/) |
| **alloyfyi** | [PyPI](https://pypi.org/project/alloyfyi/) | [npm](https://www.npmjs.com/package/alloyfyi) | **765 metal alloys, 12 families, compositions — [alloyfyi.com](https://alloyfyi.com/)** |
| gemfyi | [PyPI](https://pypi.org/project/gemfyi/) | [npm](https://www.npmjs.com/package/gemfyi) | 442 gemstones, Mohs scale, grading — [gemfyi.com](https://gemfyi.com/) |
| starfyi | [PyPI](https://pypi.org/project/starfyi/) | [npm](https://www.npmjs.com/package/starfyi) | 119,602 stars, 6,128 exoplanets, 13,305 deep-sky objects — [starfyi.com](https://starfyi.com/) |
| mineralfyi | [PyPI](https://pypi.org/project/mineralfyi/) | [npm](https://www.npmjs.com/package/mineralfyi) | 6,215 minerals, 7 crystal systems — [mineralfyi.com](https://mineralfyi.com/) |

## FYIPedia Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| colorfyi | [PyPI](https://pypi.org/project/colorfyi/) | [npm](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies — [colorfyi.com](https://colorfyi.com/) |
| emojifyi | [PyPI](https://pypi.org/project/emojifyi/) | [npm](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,953 emojis — [emojifyi.com](https://emojifyi.com/) |
| symbolfyi | [PyPI](https://pypi.org/project/symbolfyi/) | [npm](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats — [symbolfyi.com](https://symbolfyi.com/) |
| unicodefyi | [PyPI](https://pypi.org/project/unicodefyi/) | [npm](https://www.npmjs.com/package/unicodefyi) | Unicode lookup with 17 encodings — [unicodefyi.com](https://unicodefyi.com/) |
| fontfyi | [PyPI](https://pypi.org/project/fontfyi/) | [npm](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata & CSS — [fontfyi.com](https://fontfyi.com/) |
| distancefyi | [PyPI](https://pypi.org/project/distancefyi/) | [npm](https://www.npmjs.com/package/distancefyi) | Haversine distance & travel times — [distancefyi.com](https://distancefyi.com/) |
| timefyi | [PyPI](https://pypi.org/project/timefyi/) | [npm](https://www.npmjs.com/package/timefyi) | Timezone ops & business hours — [timefyi.com](https://timefyi.com/) |
| namefyi | [PyPI](https://pypi.org/project/namefyi/) | [npm](https://www.npmjs.com/package/namefyi) | Korean romanization & Five Elements — [namefyi.com](https://namefyi.com/) |
| unitfyi | [PyPI](https://pypi.org/project/unitfyi/) | [npm](https://www.npmjs.com/package/unitfyi) | Unit conversion, 220 units — [unitfyi.com](https://unitfyi.com/) |
| holidayfyi | [PyPI](https://pypi.org/project/holidayfyi/) | [npm](https://www.npmjs.com/package/holidayfyi) | Holiday dates & Easter calculation — [holidayfyi.com](https://holidayfyi.com/) |
| cocktailfyi | [PyPI](https://pypi.org/project/cocktailfyi/) | — | Cocktail ABV, calories, flavor — [cocktailfyi.com](https://cocktailfyi.com/) |
| fyipedia | [PyPI](https://pypi.org/project/fyipedia/) | — | Unified CLI: `fyi alloy info stainless-steel` — [fyipedia.com](https://fyipedia.com/) |
| fyipedia-mcp | [PyPI](https://pypi.org/project/fyipedia-mcp/) | — | Unified MCP hub for AI assistants — [fyipedia.com](https://fyipedia.com/) |

## License

MIT
