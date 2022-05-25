machine.wait_for_unit("multi-user.target")
machine.wait_for_unit("uwsgi.service")
machine.wait_for_open_port(8000)
assert "Arbeitszeit" in machine.succeed("curl -vLf 127.0.0.1:8000/")
assert "Arbeitszeit" in machine.succeed("curl -vLf 127.0.0.1:8000/member/login")
machine.succeed("curl -vLf 127.0.0.1:8000/static/main.js")
