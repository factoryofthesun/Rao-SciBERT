# -*- coding: utf-8 -*- #
# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""ai-platform operations wait command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.ml_engine import operations
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.ml_engine import endpoint_util
from googlecloudsdk.command_lib.ml_engine import flags
from googlecloudsdk.command_lib.ml_engine import operations_util


def _AddWaitArgs(parser):
  flags.OPERATION_NAME.AddToParser(parser)
  flags.GetRegionArg('operation').AddToParser(parser)


class Wait(base.CreateCommand):
  """Wait for an AI Platform operation to complete."""

  @staticmethod
  def Args(parser):
    _AddWaitArgs(parser)

  def Run(self, args):
    with endpoint_util.MlEndpointOverrides(region=args.region):
      client = operations.OperationsClient()
      return operations_util.Wait(client, args.operation)


_DETAILED_HELP = {
    'DESCRIPTION':
        """\
        Wait for an AI Platform operation to complete.

        Given an operation ID, this command polls the operation and blocks
        until it completes. At completion, the operation message is printed
        (which includes the operation response).
    """
}


Wait.detailed_help = _DETAILED_HELP
