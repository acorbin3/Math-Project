# Math-Project
This project will show the steps it takes to develop features following a DO-178 process along with going through a Problem Report process

Note - All changes shall be associated to a feature issue or a problem report issue

# Steps on introducing a feature
1. **Create an issue** -  This will be the change authorization and overview of what needs to be done for a particular feature. For an example I will create an feature issue that will add the bound function
    * For organizational purposes we can use milestones to organize a set of feature issues. For example, if we are working on a math library we might want to have separate feature issue to add in cos, sin, ceiling, floor, etc. The milestone will be the container to help track all of the issues
1. **Create branch to handle feature development** - This could be analogous to a team stream
1. **Creation of system requirements/high level requirements** - This will consist of the creation and informal review(s)
1. **Creation of software design** - This will consist of the creation and informal review(s)
1. **Creation of low level requirements** - This will consist of the creation and informal review(s)
1. **Creation of software** - This will consist of the creation and informal review(s)
1. **Creation of test cases** - This will consist of the creation and informal review(s)
1. **Creation of test procedures** - This will consist of the creation and informal review(s)
1. **Formal review of feature** - This review will cover all the changes that occurred within this feature issue

## How to handle merging
I would recommend using [Gitlab Flow](https://docs.gitlab.com/ee/workflow/gitlab_flow.html) branching mechanism. This uses a branch, do development, merge changes back into mainline. When it comes to needing releases, then we would create release branches. They call this pre-production branch, and production branch which would be a branch off pre-production.

Ideally feature branches wouldn’t be merged into the mainline until ready but since our teams are broken up into functional teams there are dependencies. That would mean 3 different process to accomplish integrated features
1. Functional teams that have feature branches would need to sync between their branches to insure proper integration. Once integration is done N teams would merge their branches into the master/trunk
1. Functional teams merge to master/trunk, do the integration and when they find problems on their side then updates would happen on their feature branch and remerge with master/trunk
1. Functional teams merge what they have to master/trunk and then re-branch to handle integration changes
1. Functional teams work on 1 feature branch and when completed and integrated then its merged into the master/trunk

The 2nd option is what we are use to and probably easily adaptable to the teams.

# Steps to a Problem Report after a baseline has occurred
I don’t think we should really be changing the problem report process
1. **Problem Report has been created** - Using a template that automatically gets populated when issue created
1. **Analysis occurs** - Engineer evaluates that this is a real problem and what might need to be fixed
1. **CCB overviews problem report** - This evaluates the PR and priorities vs others
1. **PR Opened** - Work occurs on fixing the PR. This shall be done in a separate branch.
1. **PR Fixed** - This is where the developer thinks the PR is ready to be reviewed. 
1. **PR Verified** - PR has be marked verified and ready for CCB approval on closer
1. **PR Closed** - CCB has approved the changes 

