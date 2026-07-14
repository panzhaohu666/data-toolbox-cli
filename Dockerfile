# ===== 构建阶段 =====
FROM python:3.12-slim AS builder

WORKDIR /app
COPY pyproject.toml .
COPY src/ src/
COPY README.md .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir .

# ===== 运行阶段 =====
FROM python:3.12-slim

LABEL org.opencontainers.image.title="data-toolbox-cli"
LABEL org.opencontainers.image.description="数据分析工具箱CLI"
LABEL org.opencontainers.image.source="https://github.com/panzhaohu666/data-toolbox-cli"

WORKDIR /data

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/data-toolbox /usr/local/bin/data-toolbox

ENTRYPOINT ["data-toolbox"]
