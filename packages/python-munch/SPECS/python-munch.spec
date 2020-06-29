%global modname munch

Name:               python-munch
Version:            2.5.0
Release:            2%{?dist}
Summary:            A dot-accessible dictionary (a la JavaScript objects)

License:            MIT
URL:                https://pypi.io/project/munch
Source0:            %pypi_source %{modname}

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-pbr

%global _description\
munch is a fork of David Schoonover's **Bunch** package, providing similar\
functionality. 99% of the work was done by him, and the fork was made\
mainly for lack of responsiveness for fixes and maintenance on the original\
code.\
\
Munch is a dictionary that supports attribute-style access, a la\
JavaScript.

%description %_description

%package -n python3-munch
Summary:            %{summary}
%{?python_provide:%python_provide python3-munch}

%description -n python3-munch %_description

%prep
%setup -q -n %{modname}-%{version}

# Remove shebang to make rpmlint happy.
sed -i '/\/usr\/bin\/python/d' munch/__init__.py

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-munch
%doc README.md
%{!?_licensedir:%global license %doc}
%license LICENSE.txt
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*/


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-2
- Rebuilt for Python 3.9

* Wed Mar 04 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-1
- Update to 2.5.0 (#1766566)
- Fixes build with Python 3.9 (#1789175)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-6
- Subpackage python2-munch has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Pavel Raiskup <praiskup@redhat.com> - 2.3.2-2
- add --without=python{2,3} rpmbuild options

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.3.2-1
- Update to 2.3.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-5
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.0-2
- Python 2 binary package renamed to python2-munch
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Mon Jul 31 2017 Kevin Fenzi <kevin@scrye.com> - 2.2.0-1
- Update to 2.2.0. Fixes bug #1475808

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Ralph Bean <rbean@redhat.com> - 2.1.1-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Ralph Bean <rbean@redhat.com> - 2.1.0-1
- new version

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Ralph Bean <rbean@redhat.com> - 2.0.4-1
- new version

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov 04 2015 Ralph Bean <rbean@redhat.com> - 2.0.4-1
- new version

* Sat Oct 03 2015 Ralph Bean <rbean@redhat.com> - 2.0.3-1
- new version

* Mon Aug 17 2015 Ralph Bean <rbean@redhat.com> - 2.0.2-4
- Define license macro for el6.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 Ralph Bean <rbean@redhat.com> - 2.0.2-2
- Remove shebang to make rpmlint happy.

* Sat Apr 11 2015 Ralph Bean <rbean@redhat.com> - 2.0.2-1
- Initial package for Fedora
