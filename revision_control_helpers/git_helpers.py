#!/usr/bin/env python3
"""
    Purpose:
        Library for interacting with Github and Gitlab utilizing Pythons GitPython
        Library. Wraps some normal function with some standar logging, exception
        handeling, and more
"""


# Python Library Imports
import logging
from git import Git, Repo
from git.exc import GitCommandError


"""
    Disabling this version of the function as the Repo Object gives more
    control when cloning a repository (such as branch specification.

    Keeping the code in case something here might be useful for the future)
"""
# def clone_git_repo(repo_url, destination_dir='./'):
#     """
#     Purpose:
#         Clone a Git Project Locally
#     Args:
#         repo_url (String): URL to Git Repository to be cloned (.git) link
#         destination_dir (String): Where to clone the repository
#     Return:
#         N/A
#     """
#     logging.info(f'Cloning Git Project {repo_url} into {destination_dir}')

#     try:
#         Git(destination_dir).clone(repo_url)
#     except git.exc.GitCommandError as git_err:
#         if 'Repository not found' in str(git_err):
#             logging.error('Git Repo Not Found, Failing')
#             raise
#         elif 'already exists and is not an empty directory' in str(git_err):
#             logging.warn('Git Project Already Cloned, Nothing to Do')
#         else:
#             logging.exception(
#                 f'GitCommandError Cloning Git Project: {git_err}')
#             raise
#     except Exception as err:
#         logging.exception(f'Exception Cloning Git Project: {err}')
#         raise


def clone_git_repo(repo_url, destination_dir=None, branch='master'):
    """
    Purpose:
        Clone a Git Project Locally
    Args:
        repo_url (String): URL to Git Repository to be cloned (.git) link
        destination_dir (String): Where to clone the repository
        branch (String): Branch to checkout from project
    Return:
        repo (Repo Object): Returns the cloned Repo Object
    """
    if not destination_dir:
        destination_dir =\
            './{0}/'.format(repo_url.split('/')[-1].replace('.git', ''))

    logging.info(
        f'Cloning Git Project {repo_url}:{branch} into {destination_dir}'
    )

    try:
        Repo.clone_from(repo_url, destination_dir, branch=branch)
    except GitCommandError as git_err:
        if 'Repository not found' in str(git_err):
            logging.error('Git Repo Not Found, Failing')
            raise
        elif 'not found in upstream origin' in str(git_err):
            logging.error(
                f'Git Repo Found, but branch {branch} was Not, Failing'
            )
            raise
        elif 'already exists and is not an empty directory' in str(git_err):
            logging.warning('Git Project Already Cloned, Nothing to Do')
        else:
            logging.exception(
                f'GitCommandError Cloning Git Project: {git_err}'
            )
            raise
    except Exception as err:
        logging.exception(f'Exception Cloning Git Project: {err}')
        raise

    return Repo(destination_dir)


def checkout_git_branch(project_dir='./', branch='master'):
    """
    Purpose:
        Clone a Git Project Locally
    Args:
        project_dir (String): Local location of the repository
        branch (String): Branch to checkout
    Return:
        N/A
    """

    logging.info(
        f'checking out Git Project {project_dir} -> {branch}'
    )

    try:
        repo = Repo(project_dir)
    except Exception as err:
        raise

    try:
        repo.git.checkout(branch)
    except Exception as err:
        raise
