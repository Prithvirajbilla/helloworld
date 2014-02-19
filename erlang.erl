-module(hello).
-export([world/0]).

world () ->
    io:format("Hello, world!\n").

%% hello:world().
