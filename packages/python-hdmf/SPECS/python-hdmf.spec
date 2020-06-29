%global desc %{expand: \
The Hierarchical Data Modeling Framework The Hierarchical Data Modeling
Framework, or *HDMF* is a Python package for working with hierarchical data. It
provides APIs for specifying data models, reading and writing data to different
storage backends, and representing data with Python object.Documentation of
HDMF can be found at Release. Documentation of HDMF can be found at 
https://hdmf.readthedocs.io}

%bcond_with docs

%global pypi_name hdmf

Name:           python-%{pypi_name}
Version:        1.6.2
Release:        1%{?dist}
Summary:        A package for standardizing hierarchical object data
License:        BSD
URL:            https://github.com/hdmf-dev/hdmf
Source0:        %{url}/releases/download/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%{?python_enable_dependency_generator}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-chardet
BuildRequires: python3-h5py
BuildRequires: python3-numpy
BuildRequires: python3-scipy
BuildRequires: python3-pandas
BuildRequires: python3-ruamel-yaml
BuildRequires: python3-jsonschema
BuildRequires: python3-coverage
BuildRequires: python3-flake8
BuildRequires: python3-dateutil
BuildRequires: python3-tox

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%if %{with docs}
%package doc
Summary: %{summary}
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx-gallery

%description doc
Documentation for %{name}.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

find * -type f -name "*.py" -exec sed -i '/^#![ ]*\/usr\/bin\/.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%if %{with docs}
make -C docs SPHINXBUILD=sphinx-build-3 html
rm -rf docs/build/.doctrees
rm -rf docs/build/.buildinfo
%endif

%install
%py3_install

%check
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} test.py -v

%files -n python3-%{pypi_name}
%license license.txt
%doc README.rst Legal.txt
%{_bindir}/validate_hdmf_spec
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*-py%{python3_version}.egg-info

%if %{with docs}
%files doc
%doc docs/build/html
%endif

%changelog
* Wed Jun 03 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.6.2-1
- New upstream version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-2
- Rebuilt for Python 3.9

* Tue Mar 03 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.6.1-1
- New upstream version

* Fri Feb 28 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.6.0-1
- New upstream version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.5.4-1
- New upstream version

* Wed Jan 08 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.5.1-2
- Rebuild with other source

* Wed Jan 08 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.5.1-1
- New upstream version

* Wed Jan 08 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.5.0-1
- New upstream version

* Thu Dec 19 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 1.4.0-1
- Update to v1.4.0
- Use bundled source along with the schema files
- https://github.com/hdmf-dev/hdmf/issues/195
- Use Legal.txt as a separate source as it is not included in the source tar 
- Remove unnecessary requirements

* Mon Nov 11 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.3-4
- Remove unneeded configparser BR
- https://bugzilla.redhat.com/show_bug.cgi?id=1770629
- Fix failing tests
- Include required schema files
- Re-order BRs alphabetically

* Thu Nov 07 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.3.3-3
- fix source

* Thu Nov 07 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.3.3-2
- remove legal from doc

* Thu Nov 07 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.3.3-1
- New upstream version

* Thu Oct 03 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.3.2-2
- Rebuild with new source

* Thu Oct 03 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.3.2-1
- New upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 31 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.2.0-1
- New upstream version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-2
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.1.2-1
- New upstream version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.0.5-1
- New upstream version

* Wed Jun 26 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.0.4-2
- Fix some typos

* Wed Jun 26 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.0.4-1
- New upstream version

* Tue Jun 11 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.0.3-2
- Fix BR typo

* Mon Apr 29 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.0.3-1
- New upstream version

* Sun Apr 21 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.0.2-1
- New upstream version

* Tue Mar 26 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.0.1-1
- Initial package.
