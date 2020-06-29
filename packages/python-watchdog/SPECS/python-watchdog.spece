%global modname watchdog

Name:               python-%{modname}
Version:            0.10.2
Release:            2%{?dist}
Summary:            File system events monitoring

License:            ASL 2.0 and BSD and MIT
URL:                http://pypi.python.org/pypi/%{modname}
Source0:            %pypi_source %{modname}
BuildArch:          noarch

%description
A Python API and shell utilities to monitor file system events.

%package -n python3-%{modname}
BuildArch:          noarch
BuildRequires:      python3-devel
BuildRequires:      python3-pytest
BuildRequires:      python3-pytest-cov
BuildRequires:      python3-pytest-timeout
BuildRequires:      python3-PyYAML >= 3.09
BuildRequires:      python3-argh >= 0.8.1
BuildRequires:      python3-pathtools >= 0.1.1
Summary:            %{summary}
Obsoletes:          python2-%{modname} < 0.8.3-12
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}
A Python API and shell utilities to monitor file system events.

%prep
%setup -q -n %{modname}-%{version}
# Remove all shebangs
find src -name "*.py" | xargs sed -i -e '/^#!\//, 1d'
# Remove +x of the README file
chmod -x README.rst
# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m pytest -v

%files -n python3-%{modname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*/
%{_bindir}/watchmedo*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-2
- Rebuilt for Python 3.9

* Tue Feb 18 2020 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.10.2-1
- Update to the upstream release 0.10.2
- Use the pypi_source macro for Source0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-13
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-12
- Remove python2-watchdog

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-9
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.3-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-4
- Rebuild for Python 3.6

* Mon Aug 15 2016 Julien Enselme <jujens@jujens.eu> - 0.8.3-3
- Add python-pytest-timeout to BR to launch tests

* Thu Aug 12 2016 Julien Enselme <jujens@jujens.eu> - 0.8.3-2
- Add python2-pathtools to BR (was two times in Requires)

* Thu Aug 11 2016 Julien Enselme <jujens@jujens.eu> - 0.8.3-1
- Update to 0.8.3
- Correct requires
- Update to follow new Python packaging guidelines
- Always build with Python 3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 22 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.8.2-1
- Update to 0.8.2

* Fri Apr 25 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.1-4
- Adjust the license tag to ASL2.0 and BSD and MIT

* Fri Apr 18 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.1-3
- Adjust the check for Fedora/RHEL release number for the py3 package

* Fri Apr 18 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.1-2
- Remove all shebang of the python files

* Fri Apr 18 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.1-1
- initial package for Fedora
