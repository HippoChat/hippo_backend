#!/usr/bin/env python3


def main():
    from swagger_server import app, conn, socketio

    socketio.run(app, port=8080)
    # conn.run(port=8080, threaded=True)


if __name__ == '__main__':
    main()
