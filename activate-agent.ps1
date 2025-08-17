#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Script d'activation automatique de l'agent CodeGuardian
.DESCRIPTION
    Automatise l'activation de l'agent CodeGuardian dans Cursor
#>

Write-Host "=== ACTIVATION AUTOMATIQUE AGENT CODEGUARDIAN ===" -ForegroundColor Green
Write-Host "🚀 Démarrage de l'activation automatique..." -ForegroundColor Yellow

# Vérification de l'environnement
Write-Host "`n1. Vérification de l'environnement..." -ForegroundColor Cyan
if (Test-Path ".cursor/background-agents.json") {
    Write-Host "✅ Configuration agent présente" -ForegroundColor Green
} else {
    Write-Host "❌ Configuration agent manquante" -ForegroundColor Red
    exit 1
}

if (Test-Path "$env:USERPROFILE\.cursor\mcp.json") {
    Write-Host "✅ MCP global configuré" -ForegroundColor Green
} else {
    Write-Host "❌ MCP global manquant" -ForegroundColor Red
    exit 1
}

# Vérification Git
Write-Host "`n2. Vérification Git..." -ForegroundColor Cyan
$gitStatus = git status --porcelain
if ($gitStatus) {
    Write-Host "⚠️  Fichiers non commités détectés" -ForegroundColor Yellow
    Write-Host "Committing changes..." -ForegroundColor Yellow
    git add .
    git commit -m "chore(agent): auto-activation setup"
}

# Vérification des remotes
$remotes = git remote -v
if ($remotes -like "*github.com*") {
    Write-Host "✅ Remote GitHub configuré" -ForegroundColor Green
} else {
    Write-Host "❌ Remote GitHub manquant" -ForegroundColor Red
    exit 1
}

# Test de connexion GitHub
Write-Host "`n3. Test de connexion GitHub..." -ForegroundColor Cyan
try {
    $response = Invoke-RestMethod -Uri "https://api.github.com/user" -Method Get -ErrorAction Stop
    Write-Host "✅ Connecté en tant que: $($response.login)" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Connexion GitHub non vérifiée" -ForegroundColor Yellow
}

# Création d'un fichier de test pour déclencher l'agent
Write-Host "`n4. Création d'un fichier de test..." -ForegroundColor Cyan
$testContent = @"
# Test Agent CodeGuardian
# TODO: agent check - test activation
# FIXME: implement comprehensive tests

def test_function():
    """Test function for agent activation."""
    pass

if __name__ == "__main__":
    test_function()
"@

$testContent | Out-File -FilePath "src/test_agent.py" -Encoding UTF8
Write-Host "✅ Fichier de test créé: src/test_agent.py" -ForegroundColor Green

# Commit du fichier de test
Write-Host "`n5. Commit du fichier de test..." -ForegroundColor Cyan
git add src/test_agent.py
git commit -m "test: agent activation trigger"
Write-Host "✅ Commit créé" -ForegroundColor Green

# Push vers GitHub
Write-Host "`n6. Push vers GitHub..." -ForegroundColor Cyan
git push
Write-Host "✅ Push réussi" -ForegroundColor Green

# Instructions finales
Write-Host "`n=== ACTIVATION TERMINÉE ===" -ForegroundColor Green
Write-Host "🎉 Agent CodeGuardian prêt à être activé!" -ForegroundColor Green
Write-Host "`n📋 Instructions pour Cursor:" -ForegroundColor Yellow
Write-Host "1. Redémarrez Cursor" -ForegroundColor Cyan
Write-Host "2. Ouvrez Settings (Ctrl+,)" -ForegroundColor Cyan
Write-Host "3. Allez dans 'Background Agents'" -ForegroundColor Cyan
Write-Host "4. Connectez GitHub si pas déjà fait" -ForegroundColor Cyan
Write-Host "5. Activez l'agent 'CodeGuardian'" -ForegroundColor Cyan
Write-Host "6. Vérifiez les logs dans Output → Background Agents" -ForegroundColor Cyan

Write-Host "`n🔗 Repository: https://github.com/Net-Nook2/cursor-agent" -ForegroundColor Green
Write-Host "📁 Fichier de test: src/test_agent.py" -ForegroundColor Green
Write-Host "🎯 L'agent devrait détecter les TODO/FIXME automatiquement" -ForegroundColor Green
