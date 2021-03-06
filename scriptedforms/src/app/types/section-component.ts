// Scripted Forms -- Making GUIs easy for everyone on your team.
// Copyright (C) 2017 Simon Biggs

// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at

//     http://www.apache.org/licenses/LICENSE-2.0

// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

import { StartComponent } from '../sections-module/start.component';
import { LiveComponent } from '../sections-module/live.component';
import { ButtonComponent } from '../sections-module/button.component';
import { OutputComponent } from '../sections-module/output.component';
import { SectionFileChangeComponent } from '../sections-module/section-file-change.component';

export type SectionComponent = StartComponent | LiveComponent | ButtonComponent | OutputComponent | SectionFileChangeComponent;
