from fastapi import APIRouter, HTTPException, status

from github import Github

router = APIRouter()

github = Github()

# method currently extracts all contributors for a repository and extracts their contributions
@router.get("/contributors")
def get_repo_info(repo_name : str):
    repository = github.get_repo(repo_name)

    info = {}
    contributors_info = {}

    contributor_list = repository.get_stats_contributors()
    # iterate through all contributors and return their contributions in json format
    for contributor in contributor_list:
        weekly_contribution = contributor.weeks
        current_contributor_info = {
            "Name": contributor.author.name,
            "Total number of commits":contributor.total,
            "Number of commits in the past week": weekly_contribution[-1].c,
            "Additions in the past week": weekly_contribution[-1].a,
            "Deletions in the past week": weekly_contribution[-1].d
        }
        contributors_info[contributor.author.name] = current_contributor_info

        info["Contributors"] = contributors_info
    return info