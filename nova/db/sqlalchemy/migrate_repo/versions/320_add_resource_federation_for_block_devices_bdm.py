# Copyright (c) 2016 George Silvis, III
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from sqlalchemy import String, Column, MetaData, Table


def upgrade(migrate_engine):
    meta = MetaData()
    meta.bind = migrate_engine

    bdm = Table('block_device_mapping', meta, autoload=True)
    bdm.create_column(Column('source_sp', String(255), nullable=True))
    bdm.create_column(Column('destination_sp', String(255), nullable=True))
    bdm.create_column(Column('source_project', String(255), nullable=True))
    bdm.create_column(Column('destination_project', String(255), nullable=True))
