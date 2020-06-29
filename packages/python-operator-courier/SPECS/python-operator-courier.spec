Name:           python-operator-courier
Version:        2.1.7
Release:        4%{?dist}
Summary:        Library and CLI tool to build, verify and push operator metadata

License:        ASL 2.0
URL:            https://pypi.io/project/operator-courier

Source0:        %pypi_source operator-courier

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EnablingPythonGenerators
%?python_enable_dependency_generator


%description
The operator courier library is used to build, validate and
push Operator Artifacts to quay.io application registries.

%package -n python3-operator-courier
Summary:        Library to build, verify and push operator metadata

%{?python_provide:%python_provide python3-operator-courier}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-requests
BuildRequires:  python3-PyYAML

# These are just for running tests, which will be enabled soon.
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner


%description -n python3-operator-courier
The operator courier library is used to build, validate and
push Operator Artifacts to quay.io application registries.

%prep
%autosetup -p1 -n operator-courier-%{version}

%build
%py3_build

%install
%py3_install

# No tests in the tarball yet.  Soon!
# https://github.com/operator-framework/operator-courier/issues/13
#%check
#PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest -v

%files -n python3-operator-courier
# No license in the tarball yet.  Soon!
# https://github.com/operator-framework/operator-courier/issues/13
#%%license LICENSE
%doc README.md
%{_bindir}/operator-courier
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/operatorcourier/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.7-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.7-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Martin Bašti <mbasti@redhat.com> - 2.1.7-1
- update to upstream version 2.1.7

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.5-2
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Ralph Bean <rbean@redhat.com> - 2.1.5-1
- new version

* Thu Aug 08 2019 Ralph Bean <rbean@redhat.com> - 2.1.4-1
- new version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Ralph Bean <rbean@redhat.com> - 2.1.3-1
- new version

* Fri Jun 21 2019 Ralph Bean <rbean@redhat.com> - 2.1.1-1
- new version

* Wed May 15 2019 Ralph Bean <rbean@redhat.com> - 2.0.3-1
- new version

* Tue Apr 30 2019 Ralph Bean <rbean@redhat.com> - 2.0.2-1
- new version

* Fri Apr 26 2019 Ralph Bean <rbean@redhat.com> - 2.0.1-1
- new version

* Mon Apr 01 2019 Ralph Bean <rbean@redhat.com> - 1.3.0-1
- new version

* Wed Mar 27 2019 Ralph Bean <rbean@redhat.com> - 1.2.1-1
- new version

* Tue Mar 12 2019 Ralph Bean <rbean@redhat.com> - 1.2.0-1
- new version

* Mon Mar 11 2019 Ralph Bean <rbean@redhat.com> - 1.1.0-1
- new version

* Wed Feb 27 2019 Ralph Bean <rbean@redhat.com> - 1.0.2-1
- new version

* Fri Feb 15 2019 Ralph Bean <rbean@redhat.com> - 1.0.1-1
- new version

* Mon Feb 11 2019 Ralph Bean <rbean@redhat.com> - 1.0.0-1
- Initial packaging for Fedora.
