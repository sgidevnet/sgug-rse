%{?python_enable_dependency_generator}
%global pypi_name csvkit
%global project_owner wireservice
%global github_name csvkit
%global desc csvkit is a suite of utilities for converting to and working with CSV, the king \
of tabular file formats.


Name:           python-%{pypi_name}
Version:        1.0.4
Release:        6%{?dist}
Summary:        Suite of utilities for converting to and working with CSV

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/wireservice/csvkit/archive/%{version}/csvkit-%{version}.tar.gz
# Get tests passing related to csvsql and type inference: https://github.com/wireservice/csvkit/commit/58203081e5cc828ec50f8df92cdc40f100c0b1c5
Patch0:         58203081e5cc828ec50f8df92cdc40f100c0b1c5.patch

BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist agate} >= 1.6.1
BuildRequires:  %{py3_dist agate-excel} >= 0.2.2
BuildRequires:  %{py3_dist agate-dbf} >= 0.2
BuildRequires:  %{py3_dist agate-sql} >= 0.5.3
BuildRequires:  %{py3_dist six} >= 1.6.1
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%package doc
BuildRequires:  python-sphinx-doc
BuildRequires:  python3-sphinx_rtd_theme
Summary:        %{summary}

%description doc
%{desc}

Documentation package

%prep
%setup -q -n %{github_name}-%{version}
%patch0 -p1
rm -rf *.egg-info
# Fix non-executable-script
find csvkit -name \*.py -type f | xargs sed -i '1{\@^#!/usr/bin/env python@d}'


%build
%py3_build

cd docs
make html
make man


%install
%py3_install

mkdir -p %{buildroot}%{_mandir}/man1
for file in docs/_build/man/*.1; do
    install -p -m0644 ${file} %{buildroot}%{_mandir}/man1/
done

# Remove useful files in doc
rm docs/_build/html/.buildinfo

# Correct permissions in doc
chmod -x examples/realdata/census_2000/VROUTFSJ.TXt


%check
export LC_ALL='en_US.utf8'
nosetests-%{python3_version} tests -v

%files -n python3-%{pypi_name}
%license COPYING
%doc README.rst CHANGELOG.rst AUTHORS.rst
%{_bindir}/*
%{_mandir}/man1/*
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{pypi_name}/


%files doc
%license COPYING
%doc README.rst CHANGELOG.rst AUTHORS.rst docs/_build/html examples


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-4
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Julien Enselme <jujens@jujens.eu> - 1.0.4-3
- Fix tests for mass rebuild.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 23 2019 Julien Enselme <jujens@jujens.eu> - 1.0.4-1
- Update to 1.0.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-5
- Enable python dependency generator

* Fri Dec 28 2018 Julien Enselme <jujens@jujens.eu> - 1.0.3-4
- Remove Python 2 subpackage.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.7

* Mon Mar 12 2018 Julien Enselme <jujens@jujens.eu> - 1.0.3-1
- Update to 1.0.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Jan 16 2018 Julien Enselme <jujens@jujens.eu> - 1.0.2-2
- Add missing dependency

* Sun  Oct 15 2017 Julien Enselme <jujens@jujens.eu> - 1.0.2-1
- Update to 1.0.2
- Use the %%{summary} macro
- Use the %%py2_dist and %%py3_dist macros
- Use the version instead of git tag to fetch the source on github

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11.gitbf18815
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10.gitbf18815
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 26 2016 Julien Enselme <jujens@jujens.eu> - 0.9.1-9.gitbf18815
- Fix XLSX reader

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-8.gitbf18815
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-7.gitbf18815
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 11 2016 Julien Enselme <jujens@jujens.eu> - 0.9.1-6.gitbf18815
- Correct typo in comment

* Sat Feb 6 2016 Julien Enselme <jujens@jujens.eu> - 0.9.1-5.gitbf18815
- Correct some rpmlint warnings

* Sun Jan 24 2016 Julien Enselme <jujens@jujens.eu> - 0.9.1-4.gitbf18815
- Correct build on rawhide.

* Sun Jan 24 2016 Julien Enselme <jujens@jujens.eu> - 0.9.1-3.gitbf18815
- Move unversionned binaries to python2 subpackage.

* Wed Nov 25 2015 Julien Enselme <jujens@jujens.eu> - 0.9.1-2.gitbf18815
- Add python-enum34 to the Requires for python 2 subpackage

* Mon Nov 9 2015 Julien Enselme <jujens@jujens.eu> - 0.9.1-1.gitbf18815
- Inital package
