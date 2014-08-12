# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import sys


def _CheckSubmodules():
  trace_viewer_dir = os.path.join(os.path.dirname(__file__),
                                  os.pardir,
                                  'third_party',
                                  'trace-viewer')
  if not os.listdir(trace_viewer_dir):
    sys.exit('The directory third_party/trace-viewer is empty. '
             'Please run: git submodule update --init')


def _SetupImports():
  top = os.path.join(os.path.dirname(__file__), os.pardir)
  sys.path.append(os.path.join(top,
                               'third_party'))
  sys.path.append(os.path.join(top,
                               'third_party',
			       'android_testrunner'))
  sys.path.append(os.path.join(top,
			       'third_party',
			       'trace-viewer'))
  sys.path.append(os.path.join(top,
			       'third_party',
			       'pexpect'))

_CheckSubmodules()
_SetupImports()
