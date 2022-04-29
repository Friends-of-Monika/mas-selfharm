#!/bin/sh
perl -ne 'printf $1 if /version="([^"]*)"/' mod/00_header.rpy
