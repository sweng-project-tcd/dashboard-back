from fastapi import APIRouter, HTTPException, status

from github import Github

router = APIRouter()

github = Github()

def calculate_percentage_increase(original: int, recent: int):
    if original == 0:
        return recent*100
    difference = recent - original
    difference = difference/original
    return difference*100


# method currently extracts all contributors for a repository and extracts their contributions
@router.get("/contributors")
def get_repo_info(repo_name : str):
    repository = github.get_repo(repo_name)

    info = {}
    contributors_info = {}
    stats_summary = {}

    contributor_list = repository.get_stats_contributors()
    total_commits = 0
    total_commits_this_week = 0
    total_commits_last_week = 0

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
        # add totals for summary
        total_commits_this_week = total_commits_this_week + weekly_contribution[-1].c
        total_commits = total_commits + contributor.total
        total_commits_last_week = total_commits_last_week + weekly_contribution[-2].c
        # add current contributors stats to json
        contributors_info[contributor.author.name] = current_contributor_info


    # put summary stats into json
    stats_summary = {
        "Total commits": total_commits,
        "Total commits this week": total_commits_this_week,
        "Total commits last week": total_commits_last_week,
        "Percentage increase in commits from last week": calculate_percentage_increase(total_commits_last_week, total_commits_this_week)
    }
    
    # combine both contributor and summary stats into one json
    info["Summary"] = stats_summary
    info["Contributors"] = contributors_info
    
    return info