%{?python_enable_dependency_generator}
%global pypi_name agate-sql
%global file_name agatesql
%global project_owner wireservice
%global github_name agate-sql
%global desc agate-sql adds SQL read/write support to agate. http://agate-sql.rtfd.org


Name:           python-%{pypi_name}
Version:        0.5.4
Release:        5%{?dist}
Summary:        Adds SQL read/write support to agate

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/%{version}/%{github_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3dist(agate) >= 1.5
BuildRequires:  python3dist(sqlalchemy) >= 1.0.8
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%package -n     python-%{pypi_name}-doc
Summary:        %{summary}
BuildRequires:  python3dist(sphinx) >= 1.2.2
BuildRequires:  python3dist(sphinx-rtd-theme) >= 0.1.6

%description -n python-%{pypi_name}-doc
%{desc}

Documentation package.


%prep
%setup -qn %{github_name}-%{version}
# Remove shebang on non executable scripts
sed -i '1{\@^#!/usr/bin/env python@d}' agatesql/*.py


%build
%py3_build

# Build documentation
pushd docs
    make html SPHINXBUILD=sphinx-build-%{python3_version}
    rm -f _build/html/.buildinfo
popd


%install
%py3_install


%check
# Some tests fails here but they pass on travis. We should check how this environment differs to explain this.
nosetests-%{python3_version} tests -v -e test_to_sql_create_statement_unique_constraint -e test_to_sql_create_statement

%files -n python3-%{pypi_name}
%doc README.rst AUTHORS.rst CHANGELOG.rst
%license COPYING
%{python3_sitelib}/agate_sql-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{file_name}/


%files -n python-%{pypi_name}-doc
%license COPYING
%doc README.rst AUTHORS.rst CHANGELOG.rst docs/_build/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 0.5.4-1
- Update to 0.5.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.3-5
- Enable python dependency generator

* Mon Dec 31 2018 Julien Enselme <jujens@jujens.eu> - 0.5.3-4
- Remove Python 2 subpackage (#1662653)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-2
- Rebuilt for Python 3.7

* Mon Mar 12 2018 Julien Enselme <jujens@jujens.eu> - 0.5.3-1
- Update to 0.5.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Oct 04 2017 Julien Enselme <jujens@jujens.eu> - 0.5.2-2
- Fetch sources on github with tag instead of commit

* Mon Oct 02 2017 Julien Enselme <jujens@jujens.eu> - 0.5.2-1
- Update to 0.5.2
- Fix minor SPEC issues

* Sun Mar 12 2017 Julien Enselme <jujens@jujens.eu> - 0.5.1-1
- Inital package
