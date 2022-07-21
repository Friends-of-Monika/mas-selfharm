#!/bin/sh
perl -ne 'printf $1 if /version="([^"]*)"/' mod/aa_header.rpy
