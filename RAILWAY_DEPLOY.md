# Deploy ArcReel on Railway

This is a best-effort Railway deployment setup for testing. It does not make Railway's free tier suitable for sustained video generation: resource limits and the small free volume can prevent full workflows from completing.

## Deploy

1. In Railway, create a new project and choose **Deploy from GitHub repo**.
2. Select `mksoni7777-pixel/ArcReel` and branch `railway-deploy`.
3. Let Railway build from the repository's Dockerfile. The included `railway.toml` configures the Docker build and `/health` health check.
4. Add a Railway Volume mounted at `/app/projects` before creating projects. Without a persistent volume, project files and generated media can be lost on redeploy/restart. Railway's free volume quota may be too small for videos.
5. Configure authentication and provider credentials in ArcReel's Settings UI after deployment. Do not commit API keys to GitHub.
6. In Railway service Variables, set `ARCREEL_ALLOW_UNSANDBOXED_AGENT=true` to opt into the restricted Bash allowlist fallback when Railway blocks bubblewrap namespaces. This deliberately disables the normal sandbox and is only suitable for a private, trusted single-user test deployment; do not expose it to untrusted users or projects.
7. Generate a Railway public domain and test `/health`, sign-in, project creation, and one small text-generation task before attempting image/video generation.

## Important limitations

- Railway injects `PORT`; this branch makes Uvicorn and the container health check use it, falling back to port 1241 for ordinary Docker Compose use.
- ArcReel needs substantial memory, persistent disk space, and long-running agent/generation tasks. A free/trial Railway instance may restart or run out of memory/disk.
- The app's Agent Bash sandbox requires Linux container capabilities and relaxed seccomp/AppArmor settings in the upstream Compose file. Railway does not expose every Docker host-level security option. The opt-in `ARCREEL_ALLOW_UNSANDBOXED_AGENT=true` fallback lets the server start with a restricted Bash allowlist, but is not equivalent to the normal sandbox and must only be used for a private trusted test deployment. Some agent tasks may still fail.
- Treat this as a smoke-test deployment, not a guarantee of full functionality or durable media storage. Check current Railway pricing and usage before upgrading or allowing paid usage.
