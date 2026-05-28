$ErrorActionPreference = 'Stop'

$requiredFiles = @(
  'index.html',
  'README.md',
  'CONTRIBUTING.md',
  'LICENSE',
  'assets/site.css',
  'assets/figures/abstract.svg',
  'assets/figures/simulation_framework.svg',
  'assets/figures/realism.svg',
  'data/event_camera_simulation_references.bib'
)

foreach ($file in $requiredFiles) {
  if (-not (Test-Path -LiteralPath $file)) {
    throw "Missing required file: $file"
  }
}

$readme = Get-Content -Raw 'README.md'
$entryCount = ([regex]::Matches($readme, '(?m)^- \*\*')).Count
if ($entryCount -lt 40) {
  throw "Expected at least 40 README resource entries, found $entryCount"
}

$codeLinkCount = ([regex]::Matches($readme, '\[\[code\]\(https://github\.com/')).Count
if ($codeLinkCount -lt 25) {
  throw "Expected at least 25 public GitHub code links in README, found $codeLinkCount"
}

$csvFiles = @(Get-ChildItem -LiteralPath 'data' -Filter '*.csv' -File -ErrorAction SilentlyContinue)
if ($csvFiles.Count -gt 0) {
  throw "Tabular data exports should not be published: $($csvFiles.Name -join ', ')"
}

$html = Get-Content -Raw 'index.html'
foreach ($asset in @('assets/site.css', 'assets/figures/simulation_framework.svg', 'assets/figures/realism.svg')) {
  if ($html -notlike "*$asset*") {
    throw "index.html does not reference $asset"
  }
}

if ($html -match '\.csv|assets/site\.js') {
  throw "index.html still references generated data-table assets"
}

if ($html -match 'arxiv\.org/abs/([T]ODO|[T]BD)|openreview\.net/forum\?id=([T]ODO|[T]BD)') {
  throw "index.html contains placeholder public-paper links"
}

Write-Host "site check passed: $entryCount README entries, $codeLinkCount code links, $((Get-ChildItem 'assets/figures/*.svg').Count) figure assets"
