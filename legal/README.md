# Contribution ownership process

The official open·kritt project accepts copyrightable contributions only after their
copyright has been assigned to the project owners, Harel Rom and Gabriel Balko.

Repository text, a pull-request checkbox, a DCO sign-off, or inclusion in the assignment
registry is not itself a copyright transfer. The signed agreement is the controlling
record.

## Before merging a contribution

1. The contributor completes the
   [Contributor Copyright Assignment Agreement](CONTRIBUTOR_COPYRIGHT_ASSIGNMENT.md).
2. If an employer, client, university, or other entity might own or control the work,
   that entity also completes the [Employer Disclaimer](EMPLOYER_DISCLAIMER.md).
3. Both project owners countersign the agreement and store the executed copy privately.
   Do not commit signatures, addresses, or other personal information to this public
   repository.
4. An owner adds the contributor's exact GitHub login to
   [`.github/copyright-assignment-allowlist`](../.github/copyright-assignment-allowlist)
   in a separate pull request.
5. The contributor's pull request may be merged only after the assignment-registry CI
   check passes and an owner confirms that every author and co-author is covered.

Send completed agreements and questions to `info@kritt.ai`.

## Important limits

- The automated check validates only the pull-request author's GitHub login. Owners must
  manually check co-authors, commits copied from elsewhere, employer claims, and
  third-party material.
- Dependency metadata and automated dependency-update pull requests do not assign
  ownership of third-party dependencies. Those dependencies remain under their own
  licenses and ownership.
- A contributor retains the rights that applicable law does not permit assignment or
  waiver, and receives the public project's AGPL rights like every other recipient.
- The templates in this directory must be reviewed by qualified Israeli and U.S. counsel
  before use. Repository maintainers cannot give contributors legal advice.

The contributor agreement is adapted from the
[Harmony Individual Contributor Assignment Agreement 1.0](https://www.harmonyagreements.org/agreements),
licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). It has been
substantially modified for open·kritt's ownership structure, licensing, and workflow.
