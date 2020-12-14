

# Scenario C


## Context

Two enterprises want to collaborate by sharing their Data. They want to have access to autonomous workspaces and algorithms from the marketplace. Inside this workspace, they put their data and their software.

## Prerequisites
* [Create an Autonomous Workspace]() with the following specifications:
  * Three VMs : one for each enterprise and one in common
  * SSH access for each team on their respective machine: for each team, an access on their personal VM and one on the shared VM 
* [Deploy an instance of TeraLab Marketplace]() on the Shared VM(s) 

## Instructions

### Variables

### Manual
* Login to the workspace by ssh

```bash
ssh -p ${ssh_wan_port}  ${username}@${workspace_id}.tl.teralab-datascience.fr
```
* [Configure an NFS endpoint on the shared VM]()
* [Mount the shared NFS directory on each personal VM]

## Outcome (Validation Condition):

* A workspace partitioned in three sections :
  * First team’s personal VMs : mounting NFS directory served on the shared VM
  * Second team’s personal VMs: mounting NFS directory served on the shared VM
  * A share set of VMs (both team A and B present) : 
* serving a NFS to be served and allowing both teams to share their data with each other.
  * with a Marketplace instance installed allowing them to benefit from marketplace algorithms  and data
* Since autonomous, they have sudo right, as such they can fully handle their software requirements themselves.

