#!/bin/bash
set -e  # 중간에 에러나면 스크립트 종료

echo "배포 스크립트 시작!"

cd /home/jnu/docker-compose-test

echo "기존 컨테이너 종료..."
docker compose down

echo "새 컨테이너 빌드 후 실행..."
docker compose up -d --build

echo "배포 완료!"
