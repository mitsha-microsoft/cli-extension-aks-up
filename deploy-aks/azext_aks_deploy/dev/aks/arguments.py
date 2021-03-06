# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def load_aks_arguments(self, _):
    with self.argument_context('aks up') as context:
        context.argument('pat', options_list='--pat')