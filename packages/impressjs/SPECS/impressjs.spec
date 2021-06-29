# Who knows why there are two git hashes.  Github is crazy.
# The first one is the githash on the *name* of the tarball.
# The second one is the githash of the dir that the tarball unpacks to.
%global githash gedff5a0
%global other_githash e8fbd0c
%global gitdate 20130412
%global checkout %{gitdate}git%{githash}

Name:       impressjs
Version:    0.5.3
Release:    11.%{checkout}%{?dist}
Summary:    Javascript presentation framework
BuildArch:  noarch

# It is dual licensed under the MIT and GPL
# https://github.com/bartaz/impress.js/issues/279
License:    MIT or GPLv2+

URL:        http://bartaz.github.io/impress.js
Source0:    https://github.com/bartaz/impress.js/tarball/%{version}/bartaz-impress.js-%{version}-0-%{githash}.tar.gz

# The demo that we ship in %%doc expects impress.js to be in a certain
# location.  Here we patch that html demo to look for impress.js in
# %%{_datadir} where we actually install it.
Patch0:     impressjs-patch-demo-url.patch

%description
It's a presentation framework based on the power of CSS3 transforms and
transitions in modern browsers and inspired by the idea behind prezi.com.

%prep
%setup -q -cn bartaz-impress.js-%{githash}
mv bartaz-impress.js-%{other_githash}/* .
%patch0 -p1 -b .demo-url

%build
# Nothing to actually do here.

%install
# Simply copy files into place
%{__mkdir_p} %{buildroot}%{_datadir}/impressjs
install -D -m 0644 js/impress.js %{buildroot}%{_datadir}/impressjs/impress.js

%files
%doc README.md index.html css/
%{_datadir}/impressjs/

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-11.20130412gitgedff5a0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10.20130412gitgedff5a0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-9.20130412gitgedff5a0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8.20130412gitgedff5a0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7.20130412gitgedff5a0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-6.20130412gitgedff5a0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-5.20130412gitgedff5a0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4.20130412gitgedff5a0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3.20130412gitgedff5a0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2.20130412gitgedff5a0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 18 2013 Ralph Bean <rbean@redhat.com> - 0.5.3-1.20130412gitgedff5a0
- Initial packaging for Fedora
- Added comment on the patch.
- Changed release number as per package review (#951711).
- Use install instead of cp.
