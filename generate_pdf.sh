#!/bin/bash

# Copyright (c) 2023 - for information on the respective copyright owner
# see the NOTICE file and/or the repository
# https://github.com/catenax-eV/cx-odrl-profile
#
# SPDX-License-Identifier: Apache-2.0


# https://learnbyexample.github.io/customizing-pandoc/#changing-settings-via-v-option

pandoc -f gfm -V linkcolor:blue -V geometry:margin=2.5cm --toc -o profile.pdf profile.md
