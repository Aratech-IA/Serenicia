import argparse
import asyncio
import json
import logging
import os
import ssl
import uuid
import numpy as np

import cv2
from aiohttp import web
from av import VideoFrame

from aiortc import MediaStreamTrack, RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaBlackhole, MediaPlayer, MediaRecorder

ROOT = os.path.dirname(__file__)

logger = logging.getLogger("pc")
pcs = set()


class VideoTransformTrack(MediaStreamTrack):
    """
    A video stream track that transforms frames from an another track.
    """

    kind = "video"

    def __init__(self, track):
        super().__init__()  # don't forget this!
        self.track = track

    async def recv(self):
        frame = await self.track.recv()
        img = frame.to_ndarray(format="bgr24")
        logo = cv2.imread('./static/app7_video/img/watermark.png')
        logo = cv2.resize(logo, (100, 60))  # width, height
        # Create a mask of logo
        img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
        # Region of Image (ROI), where we want to insert logo
        roi = img[-60 - 10:-10, -100 - 10:-10]  # height box, shift bottom:top, width box, shift right:left
        # NOTE  it seems that shift values must be equal
        # Set an index of where the mask is
        roi[np.where(mask)] = 0
        roi += logo
        new_frame = VideoFrame.from_ndarray(img, format="bgr24")
        new_frame.pts = frame.pts
        new_frame.time_base = frame.time_base

        return new_frame


async def index(request):
    content = open(os.path.join(ROOT, "templates/app7_video/index_copy.html"), "r").read()
    return web.Response(content_type="text/html", text=content)


async def javascript(request):
    content = open(os.path.join(ROOT, "static/app7_video/js/client.js"), "r").read()
    return web.Response(content_type="application/javascript", text=content)


async def offer(request):
    params = await request.json()
    offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])
    pc = RTCPeerConnection()
    # pc_id = "PeerConnection(%s)" % uuid.uuid4()
    pcs.add(pc)

    # def log_info(msg, *args):
    #     logger.info(pc_id + " " + msg, *args)
    #
    # log_info("Created for %s", request.remote)

    @pc.on("track")
    def on_track(track):
        # log_info("Track %s received", track.kind)
        if track.kind == "audio":
            pc.addTrack(track)
            recorder.addTrack(track)
        elif track.kind == "video":
            local_video = VideoTransformTrack(track)
            pc.addTrack(local_video)
            recorder.addTrack(track)

        @track.on("ended")
        async def on_ended():
            # log_info("Track %s ended", track.kind)
            await recorder.stop()
    ifrecord=params["ifrecord"]
    filename=params["filename"]
    if ifrecord:
        recorder = MediaRecorder(filename)
    else:
        recorder = MediaBlackhole()

    # handle offer
    await pc.setRemoteDescription(offer)
    await recorder.start()

    # send answer
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return web.Response(
        content_type="application/json",
        text=json.dumps(
            {"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}
        ),
    )

async def on_shutdown(app):
    # close peer connections
    coros = [pc.close() for pc in pcs]
    print(f'il est ou le coros il ou {coros}')
    await asyncio.gather(*coros)
    pcs.clear()


# def webRTC():
#     parser = argparse.ArgumentParser(
#         description="WebRTC audio / video / data-channels demo"
#     )
#     parser.add_argument("--cert-file", default="/etc/letsencrypt/live/dev.serenicia.fr/fullchain.pem",
#                         help="SSL certificate file (for HTTPS)")
#     parser.add_argument("--key-file", default="/etc/letsencrypt/live/dev.serenicia.fr/privkey.pem",
#                         help="SSL key file (for HTTPS)")
#     parser.add_argument(
#         "--host", default="0.0.0.0", help="Host for HTTP server (default: 0.0.0.0)"
#     )
#     parser.add_argument(
#         "--port", type=int, default=8090, help="Port for HTTP server (default: 8080)"
#     )
#     parser.add_argument("--record-to", help="Write received media to a file.")
#     parser.add_argument("--verbose", "-v", action="count")
#     parser.add_argument("--write-audio", help="Write received audio to a file")
#     args = parser.parse_args()
#     # ifrecord = params["ifrecord"]
#     # # ifrecord = True
#     # if ifrecord:
#     #     recorder = MediaRecorder("testvideofdv.mp4")
#     # else:
#     #     recorder = MediaBlackhole()
#
#     if args.verbose:
#         logging.basicConfig(level=logging.ERROR)
#     else:
#         logging.basicConfig(level=logging.INFO)
#
#     if args.cert_file:
#         ssl_context = ssl.SSLContext()
#         ssl_context.load_cert_chain(args.cert_file, args.key_file)
#     else:
#         ssl_context = None
#
#     app = web.Application()
#     app.on_shutdown.append(on_shutdown)
#     app.router.add_get("/", index)
#     app.router.add_get("/client.js", javascript)
#     app.router.add_post("/offer", offer)
#     web.run_app(
#         app, access_log=None, host=args.host, port=args.port, ssl_context=ssl_context
#     )
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="WebRTC audio / video / data-channels demo"
    )
    parser.add_argument("--cert-file", default="/etc/letsencrypt/live/dev.serenicia.fr/fullchain.pem", help="SSL certificate file (for HTTPS)")
    parser.add_argument("--key-file", default="/etc/letsencrypt/live/dev.serenicia.fr/privkey.pem", help="SSL key file (for HTTPS)")
    parser.add_argument(
        "--host", default="0.0.0.0", help="Host for HTTP server (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--port", type=int, default=8090, help="Port for HTTP server (default: 8080)"
    )
    parser.add_argument("--record-to", help="Write received media to a file.")
    parser.add_argument("--verbose", "-v", action="count")
    parser.add_argument("--write-audio", help="Write received audio to a file")
    args = parser.parse_args()
    # ifrecord = params["ifrecord"]
    # # ifrecord = True
    # if ifrecord:
    #     recorder = MediaRecorder("testvideofdv.mp4")
    # else:
    #     recorder = MediaBlackhole()

    if args.verbose:
        logging.basicConfig(level=logging.ERROR)
    else:
        logging.basicConfig(level=logging.INFO)

    if args.cert_file:
        ssl_context = ssl.SSLContext()
        ssl_context.load_cert_chain(args.cert_file, args.key_file)
    else:
        ssl_context = None

    app = web.Application()
    app.on_shutdown.append(on_shutdown)
    app.router.add_get("/", index)
    app.router.add_get("/client.js", javascript)
    app.router.add_post("/offer/", offer)
    web.run_app(
        app, access_log=None, host=args.host, port=args.port, ssl_context=ssl_context
    )
