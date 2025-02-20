<!doctype html>
<html>
    <head>
	<title>[% nodename %] - Proxmox Console</title>
	<link rel="stylesheet" href="/xtermjs/xterm.css?version=1.0-5" />
	<link rel="stylesheet" href="/xtermjs/style.css?version=1.0-5" />
	<script src="/xtermjs/xterm.js?version=1.0-5" ></script>
	<script src="/xtermjs/fit.js?version=1.0-5" ></script>
	<script src="/xtermjs/util.js?version=1.0-5" ></script>
    </head>
    <body>
	<div id="status_bar"></div>
	<div id="wrap">
	<div id="terminal-container"></div>
	</div>
	<script type="text/javascript">
	    if (typeof(PVE) === 'undefined') PVE = {};
	    PVE.UserName = '[% username %]';
	    PVE.CSRFPreventionToken = '[% token %]';
	</script>
	<script src="/xtermjs/main.js?version=1.0-5" defer ></script>
    </body>
</html>
