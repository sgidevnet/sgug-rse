%global srcname sphinx-issues

Name:           python-%{srcname}
Version:        1.2.0
Release:        6%{?dist}
Summary:        Sphinx extension for linking to your project's issue tracker

License:        MIT
URL:            https://github.com/sloria/sphinx-issues
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description
A Sphinx extension for linking to your project's issue tracker. Includes roles
for linking to issues, pull requests, user profiles, with built-in support for
GitHub (though this works with other services).


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A Sphinx extension for linking to your project's issue tracker. Includes roles
for linking to issues, pull requests, user profiles, with built-in support for
GitHub (though this works with other services).


%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/sphinx_issues.py
%{python3_sitelib}/sphinx_issues-%{version}-py?.?.egg-info


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- Initial package.
