#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Script de vérification de l'état de l'agent CodeGuardian
#>

Write-Host "=== VÉRIFICATION ÉTAT AGENT CODEGUARDIAN ===" -ForegroundColor Green

# Vérification des fichiers de configuration
Write-Host "`n1. Configuration:" -ForegroundColor Cyan
if (Test-Path ".cursor/background-agents.json") {
    Write-Host "✅ Configuration agent présente" -ForegroundColor Green
} else {
    Write-Host "❌ Configuration agent manquante" -ForegroundColor Red
}

if (Test-Path "$env:USERPROFILE\.cursor\mcp.json") {
    Write-Host "✅ MCP global configuré" -ForegroundColor Green
} else {
    Write-Host "❌ MCP global manquant" -ForegroundColor Red
}

# Vérification Git
Write-Host "`n2. Git:" -ForegroundColor Cyan
$remotes = git remote -v
if ($remotes -like "*github.com*") {
    Write-Host "✅ Remote GitHub configuré" -ForegroundColor Green
} else {
    Write-Host "❌ Remote GitHub manquant" -ForegroundColor Red
}

$currentBranch = git branch --show-current
Write-Host "✅ Branche actuelle: $currentBranch" -ForegroundColor Green

# Vérification des fichiers de test
Write-Host "`n3. Fichiers de test:" -ForegroundColor Cyan
if (Test-Path "src/test_agent.py") {
    Write-Host "✅ Fichier de test présent" -ForegroundColor Green
    $todoCount = (Get-Content "src/test_agent.py" | Select-String "TODO|FIXME").Count
    Write-Host "✅ TODO/FIXME détectés: $todoCount" -ForegroundColor Green
} else {
    Write-Host "❌ Fichier de test manquant" -ForegroundColor Red
}

# Instructions
Write-Host "`n=== INSTRUCTIONS ===" -ForegroundColor Green
Write-Host "1. Redémarrez Cursor" -ForegroundColor Cyan
Write-Host "2. Settings → Background Agents" -ForegroundColor Cyan
Write-Host "3. Connectez GitHub" -ForegroundColor Cyan
Write-Host "4. Activez l'agent CodeGuardian" -ForegroundColor Cyan
Write-Host "5. Vérifiez les logs: Output → Background Agents" -ForegroundColor Cyan

Write-Host "`n🔗 Repository: https://github.com/Net-Nook2/cursor-agent" -ForegroundColor Green
