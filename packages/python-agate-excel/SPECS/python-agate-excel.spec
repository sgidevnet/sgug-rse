%{?python_enable_dependency_generator}
%global pypi_name agate-excel
%global file_name agateexcel
%global project_owner wireservice
%global github_name agate-excel
%global desc Adds read support for Excel files (xls and xlsx) to agate. \
See: http://agate-excel.rtfd.org


Name:           python-%{pypi_name}
Version:        0.2.3
Release:        5%{?dist}
Summary:        Adds read support for Excel files to agate

License:        MIT
URL:            https://pypi.python.org/pypi/agate-excel
Source0:        https://github.com/wireservice/agate-excel/archive/%{version}/agate-excel-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose >= 1.1.2
BuildRequires:  python3dist(agate) >= 1.5
BuildRequires:  python3dist(xlrd) >= 0.9.4
BuildRequires:  python3dist(openpyxl) >= 2.3

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%package -n     python-%{pypi_name}-doc
Summary:        %{summary}
BuildRequires:  python3dist(sphinx) >= 1.2.2
BuildRequires:  python3dist(sphinx-rtd-theme) >= 0.1.6
BuildArch:      noarch

%description -n python-%{pypi_name}-doc
%{desc}

Documentation package.


%prep
%setup -qn %{github_name}-%{version}
# Remove shebang on non executable scripts
sed -i '1{\@^#!/usr/bin/env python@d}' agateexcel/*.py


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
nosetests-%{python3_version} tests -v


%files -n python3-%{pypi_name}
%doc README.rst AUTHORS.rst CHANGELOG.rst
%license COPYING
%{python3_sitelib}/agate_excel-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{file_name}/


%files -n python-%{pypi_name}-doc
%license COPYING
%doc README.rst AUTHORS.rst CHANGELOG.rst docs/_build/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 23 2019 Julien Enselme <jujens@jujens.eu> - 0.2.3-1
- Update to 0.2.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-5
- Enable python dependency generator

* Mon Dec 31 2018 Julien Enselme <jujens@jujens.eu> - 0.2.2-4
- Remove Python 2 subpackage (#1662646)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-2
- Rebuilt for Python 3.7

* Mon Mar 12 2018 Julien Enselme <jujens@jujens.eu> - 0.2.2-1
- Update to 0.2.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Julien Enselme <jujens@jujens.eu> - 0.2.1-2
- Fetch sources on github with tag instead of commit

* Sun Mar 12 2017 Julien Enselme <jujens@jujens.eu> - 0.2.1-1
- Inital package
