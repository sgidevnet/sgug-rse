Name:		asciinema
Version:	2.0.1
Release:	7%{?dist}
Summary:	Terminal session recorder
License:	GPLv3+
URL:		https://asciinema.org
Source0:	https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	python%{python3_pkgversion}-setuptools
BuildRequires:	python%{python3_pkgversion}-nose
# pkg_resources is used from /usr/bin/asciinema
Requires:       python%{python3_pkgversion}-setuptools


%description
Asciinema is a free and open source solution for recording the terminal sessions
and sharing them on the web.


%prep
%setup -q -n %{name}-%{version}


%build
%py3_build


%install
%py3_install

# man page
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/asciinema.1 %{buildroot}%{_mandir}/man1/


%check
# setup.py runs `nosetests` command only, we need to specify python version
#%{__python3} setup.py test
nosetests-%{python3_version} -v


%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/asciinema
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info/
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-5
- Add setuptools back to requires

* Mon Aug 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-4
- Fixup license tag
- Trivial cleanups in packaging

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.7

* Mon Apr 16 2018 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 2.0.1-1
- Update to version 2.0.1

* Mon Feb 12 2018 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 2.0.0-1
- Update to version 2.0.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 1.4.0-1
- Update to version 1.4.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jul 17 2016 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 1.3.0-1
- update to version 1.3.0
- Rewritten from Go to python3

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun  3 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 1.1.0-1
- Update to new version

* Mon Mar 23 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 1.0.0-2
- Patch: support locale which ends with utf8
- Patch: edit some details in man page

* Tue Mar 17 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 1.0.0-1
- Update to new version
- Add Godeps to docs

* Fri Mar  6 2015 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.9-1
- Update to new version
- Rewritten to Go
- License changed to GPLv3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.8-1
- Update to new version

* Mon Jan 27 2014 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.7-3
- Add check of tests
- Add build and common requires
- Patch for non-interactive shell

* Mon Dec  2 2013 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.7-2
- A few spec file changes
- Edit Summary

* Mon Nov 25 2013 Jakub Jedelsky <jakub.jedelsky@gmail.com> - 0.9.7-1
- Initial package
