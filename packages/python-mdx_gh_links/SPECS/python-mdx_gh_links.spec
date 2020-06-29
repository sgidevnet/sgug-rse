%global pypiname mdx_gh_links
%global projname github-links

Name:           python-%{pypiname}
Version:        0.2
Release:        3%{?dist}
Summary:        Python-Markdown Github-Links Extension

License:        BSD
URL:            https://github.com/Python-Markdown/%{projname}/
Source0:        https://github.com/Python-Markdown/%{projname}/archive/%{version}.tar.gz#/%{projname}-%{version}.tar.gz

BuildArch:      noarch


%global _description %{expand:
This package provides an extension to Python-Markdown which adds support for
shorthand links to GitHub users, repositories, issues and commits.}

%description %_description

%package -n python3-%{pypiname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypiname}}
BuildRequires:  python3-markdown

%description -n python3-%{pypiname} %_description

%prep
%autosetup -n %{projname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} test_gh_links.py

%files -n python3-%{pypiname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypiname}-*.egg-info/
%{python3_sitelib}/%{pypiname}.py
%{python3_sitelib}/__pycache__/*

%changelog
* Thu Jun 25 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.2-3
- BR python3dist(setuptools)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2-2
- Rebuilt for Python 3.9

* Sun Mar  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.2-1
- Initial packaging
