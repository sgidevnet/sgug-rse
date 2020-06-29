%global srcname markdown2

Name:           python-%{srcname}
Version:        2.3.9
Release:        3%{?dist}
Summary:        A fast and complete Python implementation of Markdown
License:        MIT
URL:            https://github.com/trentm/python-%{srcname}/
Source0:        https://pypi.io/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pygments
BuildRequires:  python3-setuptools


%description
Markdown is a text-to-HTML filter; it translates an easy-to-read /
easy-to-write structured text format into HTML. Markdown's text format
is most similar to that of plain text email, and supports features
such as headers, emphasis, code blocks, blockquotes, and links.

This is a fast and complete Python implementation of the Markdown
spec.

For information about markdown itself, see
http://daringfireball.net/projects/markdown/


%package -n python3-%{srcname}
Summary:        A fast and complete Python implementation of Markdown
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Markdown is a text-to-HTML filter; it translates an easy-to-read /
easy-to-write structured text format into HTML. Markdown's text format
is most similar to that of plain text email, and supports features
such as headers, emphasis, code blocks, blockquotes, and links.

This is a fast and complete Python implementation of the Markdown
spec.

For information about markdown itself, see
http://daringfireball.net/projects/markdown/


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%py3_build


%install
%py3_install

# remove shebangs and fix permissions
find %{buildroot}%{python3_sitelib} \
  \( -name '*.py' -o -name 'py.*' \) \
  -exec sed -i '1{/^#!/d}' {} \; \
  -exec chmod u=rw,go=r {} \;


%check
pushd test
%{__python3} test.py -- -knownfailure %{?skip_tests} || :
popd


%files -n python3-%{srcname}
%doc CHANGES.md
%doc CONTRIBUTORS.txt
%doc TODO.txt
%license LICENSE.txt
%{python3_sitelib}/*
%exclude %dir %{python3_sitelib}/__pycache__
%{_bindir}/%{srcname}


%changelog
* Wed Jun 24 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.9-3
- Add explicit BR on python3-setuptools.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.9-2
- Rebuilt for Python 3.9

* Sat May 16 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.9-1
- Update to 2.3.9.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.8-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.8-4
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.8-3
- Drop Python2 subpackage.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul  7 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.8-1
- Update to 2.3.8.

* Sat Feb  9 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.7-1
- Update to 2.3.7.
- Simplify spec file.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 29 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.6-1
- Update to 2.3.6.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.5-4
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.5-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.5-1
- Update to 2.3.5.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May  1 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.4-1
- Update to 2.3.4.
- Update source URL.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.3.1-2
- Rebuild for Python 3.6

* Tue Nov 15 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.1-1
- Update to 2.3.1.
- Do not own top-level __pycache__ dir.
- Do not fail build on failed tests.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.0-4
- Follow updated Python packaging guidelines.
- Mark license file as %%license.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 25 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.0-1
- Update to 2.3.0.

* Fri Sep  5 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.3-1
- Update to 2.2.3.

* Fri Aug 22 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.2-1
- Update to 2.2.2.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Mar  8 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.1-1
- Update to 2.2.1.

* Wed Feb  5 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.0-1
- Update to 2.2.0.
- Modernize spec file.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct  4 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.0-1
- Update to 2.1.0.

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 2.0.1-2
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Jul 27 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.1-1
- Update to 2.0.1.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.0-1
- Update to 2.0.0.

* Sat May 19 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.2-2
- Skip pygments test on rhel6.

* Sat May 19 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.2-1
- Update to 1.4.2.
- Build python3 subpackage.

* Fri Mar 16 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.1-1
- Update to 1.1.1.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.1.19-1
- Update to 1.0.1.19.
  - Drop patch applied upstream.
  - Update project URL.
- Update macros, use %%global.
- Update %%doc.
- Do not run tests known to fail.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun  3 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.1.17-1
- Update to 1.0.17.
- Add patch for failing test.

* Tue Dec 29 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.1.16-2
- Patch for older pygments on rhel no longer needed, pygments has been
  updated in EPEL.

* Fri Dec 18 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.1.16-1
- Update to 1.0.1.16.

* Thu Oct  8 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.1.15-1
- Update to 1.0.1.15. Fixes three issues, two of them being
  security-related.

* Wed Sep  2 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.1.13-3
- Patch syntax_color test case for older pygments version on rhel.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.1.13-1
- Update to 1.0.1.13.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.1.11-2
- Rebuild for Python 2.6

* Wed Oct  1 2008 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.1.11-1
- Update to 1.0.11, also fixes the syntax_color test for the latest
  Pygments (should fix FTBFS bug 465049).

* Fri Sep 26 2008 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.1.10-1
- Update to 1.0.1.10.

* Fri Sep 12 2008 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.1.9-1
- Update to 1.0.1.9.

* Thu Sep 11 2008 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.1.8-1
- Update to 1.0.1.8.
- Simplify the cmdline wrapper.

* Tue Sep  9 2008 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.1.7-1
- New package.
