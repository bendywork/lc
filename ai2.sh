#!/bin/bash

echo "请选择要启动的工具："
echo "1) Claude"
echo "2) Codex"

read -p "输入选项 (1/2): " choice

case $choice in
  1)
    echo "启动 Claude..."

    http_proxy=http://127.0.0.1:7897 \
    https_proxy=http://127.0.0.1:7897 \
    ANTHROPIC_AUTH_TOKEN=sk-UrHldCrF1tZEl1iix7d6J8aR1Du3VyIUziOds4cX5JO7YRGC \
    ANTHROPIC_BASE_URL=https://api.01122002.xyz/ \
    ANTHROPIC_MODEL=glm-5.1 \
    claude --dangerously-skip-permissions
    ;;
    
  2)
    echo "启动 Codex..."

    http_proxy=http://127.0.0.1:7897 \
    https_proxy=http://127.0.0.1:7897 \
    OPENAI_API_KEY=wcg2026 \
    OPENAI_BASE_URL=http://localhost:9090/v1 \
    OPENAI_MODEL=gpt-5.4 \
    codex -- --full-auto
    ;;
    
  *)
    echo "无效选项，请输入 1 或 2"
    exit 1
    ;;
esac