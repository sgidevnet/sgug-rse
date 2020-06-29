%global pkgname pygit2

Name:           python-%{pkgname}
Version:        1.2.1
Release:        1%{?dist}
Summary:        Python bindings for libgit2

License:        GPLv2 with linking exception
URL:            https://www.pygit2.org/
Source0:        https://github.com/libgit2/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  (libgit2-devel >= 1.0.0 with libgit2-devel < 2.0.0)

%description
pygit2 is a set of Python bindings to the libgit2 library, which implements
the core of Git.


%package -n     python3-%{pkgname}
Summary:        Python 3 bindings for libgit2
%{?python_provide:%python_provide python3-%{pkgname}}
BuildRequires:  python3-cffi
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-cached_property

%description -n python3-%{pkgname}
pygit2 is a set of Python bindings to the libgit2 library, which implements
the core of Git.

The python3-%{pkgname} package contains the Python 3 bindings.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
BuildRequires:  /usr/bin/sphinx-build

%description    doc
Documentation for %{name}.


%prep
%autosetup -n %{pkgname}-%{version} -p1


%build
%py3_build

make -C docs html


%install
%py3_install
find %{_builddir} -name '.buildinfo' -print -delete


%check
# This is horrible, but otherwise pytest does not use pygit2 from site-packages
rm -f pygit2/__init__.py
# https://github.com/libgit2/pygit2/issues/812
%ifarch ppc64 s390x
  PYTHONPATH=%{buildroot}%{python3_sitearch} py.test-%{python3_version} -v || :
%else
  PYTHONPATH=%{buildroot}%{python3_sitearch} py.test-%{python3_version} -v
%endif


%files -n python3-%{pkgname}
%license COPYING
%doc README.rst
%{python3_sitearch}/%{pkgname}-*.egg-info/
%{python3_sitearch}/%{pkgname}/

%files doc
%license COPYING
%doc docs/_build/html/*


%changelog
* Fri Jun 05 2020 Pete Walter <pwalter@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Sat Mar 21 2020 Pete Walter <pwalter@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Tue Mar 03 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Sun Feb 02 2020 Pete Walter <pwalter@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Pete Walter <pwalter@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.28.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.28.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 14:32:34 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.28.2-1
- Update to 0.28.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Pete Walter <pwalter@fedoraproject.org> - 0.27.4-1
- Update to 0.27.4
- Enable tests on aarch64 as they seem fixed now

* Thu Dec 27 2018 Pete Walter <pwalter@fedoraproject.org> - 0.27.3-1
- Update to 0.27.3
- Switch to pytest

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.27.2-2
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Sep 17 2018 Pete Walter <pwalter@fedoraproject.org> - 0.27.2-1
- Update to 0.27.2

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.27.1-1
- Update to 0.27.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.26.4-2
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Pete Walter <pwalter@fedoraproject.org> - 0.26.4-1
- Update to 0.26.4

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.26.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 26 2017 Pete Walter <pwalter@fedoraproject.org> - 0.26.3-1
- Update to 0.26.3

* Fri Dec 01 2017 Pete Walter <pwalter@fedoraproject.org> - 0.26.2-1
- Update to 0.26.2

* Mon Nov 20 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.26.1-3
- Fixup python3 conditionals

* Mon Nov 20 2017 Pete Walter <pwalter@fedoraproject.org> - 0.26.1-2
- Add back Python 3 conditionals

* Mon Nov 20 2017 Pete Walter <pwalter@fedoraproject.org> - 0.26.1-1
- Update to 0.26.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.26.0-1
- Update to 0.26.0

* Sun May 07 2017 Pete Walter <pwalter@fedoraproject.org> - 0.25.1-2
- Fix the build with cffi 1.10

* Thu Apr 27 2017 Pete Walter <pwalter@fedoraproject.org> - 0.25.1-1
- Update to 0.25.1
- Disable one more failing test that tries to do network access

* Mon Apr 10 2017 Pete Walter <pwalter@fedoraproject.org> - 0.25.0-3
- Trivial spec file fixes
- Add Python 3 conditionals

* Tue Feb 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.25.0-2
- Bump release for rebuild

* Tue Jan 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.25.0-1
- Update to 0.25.0 (RHBZ #1408689)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.24.2-2
- Rebuild for Python 3.6

* Sat Nov 19 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.24.2-1
- Update to 0.24.2 (RHBZ #1390796)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 22 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.24.1-1
- Update to 0.24.1 (RHBZ #1348750)

* Mon Apr 18 2016 Igor Gnatenko <ignatenko@redhat.com> 0.24.0-3
- Remove remote-calling unit tests
- repository: decode() linkname
- repository: SYMTYPE is constant in module tarfile, not in any class

* Thu Apr 14 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.24.0-2
- Add python[23]-six to BR/Rs

* Sun Mar 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.24.0-1
- Update to 0.24.0

* Wed Feb 24 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.23.3-2
- Fix building 0.23.3 also in i686

* Sun Feb 14 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.23.3-1
- Update to 0.23.3
- Fix compliance with new packaging guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Sep 27 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.23.1-1
- Update to 0.23.1 (RHBZ #1266726)

* Fri Jul 31 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.23.0-0.1
- Cherry-pick patch for 0.23.0 support

* Fri Jul 31 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.22.1-2
- Rebuilt for libgit2-0.23.0 and libgit2-glib-0.23

* Mon Jul 13 2015 Mathieu Bridon <bochecha@daitauha.fr> - 0.22.1-1
- Update to 0.22.1 (#1242226)
- Drop one of our patches, as it has been merged in this release.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 21 2015 Mathieu Bridon <bochecha@daitauha.fr> - 0.22.0-1
- Update to 0.22.0

* Mon Nov 17 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 0.21.4-1
- Update to 0.21.4

* Fri Sep 19 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 0.21.3-1
- Update to 0.21.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 0.21.2-2
- Add missing requirement
  https://bugzilla.redhat.com/show_bug.cgi?id=1129868

* Tue Aug 12 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 0.21.2-1
- Update to 0.21.2

* Tue Jul 29 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 0.21.1-1
- Update to 0.21.1

* Sun Jun 29 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 0.21.0-1
- Update to 0.21.0

* Sat Jun 21 2014 Christopher Meng <rpm@cicku.me> - 0.20.3-1
- Update to 0.20.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Mar 09 2014 Christopher Meng <rpm@cicku.me> - 0.20.2-1
- Update to 0.20.2

* Sun Dec 08 2013 Christopher Meng <rpm@cicku.me> - 0.20.0-1
- Update to 0.20.0
- Clarify the license

* Tue Oct 08 2013 Christopher Meng <rpm@cicku.me> - 0.19.1-2
- Split out -doc subpackage.
- Correct the libs permissions.

* Mon Oct 07 2013 Christopher Meng <rpm@cicku.me> - 0.19.1-1
- Update to 0.19.1

* Sat Aug 17 2013 Christopher Meng <rpm@cicku.me> - 0.19.0-4
- Add missing sphinx BR.

* Tue Aug 13 2013 Christopher Meng <rpm@cicku.me> - 0.19.0-3
- Remove unneeded files.

* Mon Aug 12 2013 Christopher Meng <rpm@cicku.me> - 0.19.0-2
- Add missing nose BR.
- Add docs.

* Thu Aug 01 2013 Christopher Meng <rpm@cicku.me> - 0.19.0-1
- Update to new release.

* Fri Apr 26 2013 Christopher Meng <rpm@cicku.me> - 0.18.1-1
- Update to new release.

* Mon Sep 24 2012 Christopher Meng <rpm@cicku.me> - 0.17.3-1
- Update to new release.

* Sun Jul 29 2012 Christopher Meng <rpm@cicku.me> - 0.17.2-1
- Update to new release.

* Fri Mar 30 2012 Christopher Meng <rpm@cicku.me> - 0.16.1-1
- Update to new release.

* Thu Mar 01 2012 Christopher Meng <rpm@cicku.me> - 0.16.0-1
- Initial Package.
