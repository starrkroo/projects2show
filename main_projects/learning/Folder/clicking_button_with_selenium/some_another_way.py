#!/usr/bin/env python3

from ghost import Ghost
ghost = Ghost()

with ghost.start() as session:
  page, extra_resources = ghost.open("http://jeanphi.me")
  assert page.http_status==200 and 'jeanphix' in ghost.content
