%global srcname mimerender

Name:           python-%{srcname}
Version:        0.6.0
Release:        8%{?dist}
Summary:        RESTful HTTP Content Negotiation for Flask, Bottle, etc.

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.python.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
# License file is now in the *repo* but not the *tarball*...
Source1:        https://github.com/martinblech/mimerender/blob/v%{version}/LICENSE

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-mimeparse
BuildRequires:  python3-setuptools

%description
mimerender provides a decorator that wraps a HTTP request handler to select
the correct render function for a given HTTP Accept header. It uses mimeparse
to parse the accept string and select the best available representation.
Supports Flask, Bottle, web.py and webapp2 out of the box, and it’s easy to
add support for other frameworks.


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-mimeparse
# Note: mimerender has subclasses of MimeRenderBase for web.py, Flask,
# Bottle, and webapp2. When you import 'mimerender', the subclass for
# each framework you have installed will be defined; if the framework
# isn't installed, the subclass for it is skipped (they're all in try/
# except blocks). So if you have python3-flask installed you'll get
# the FlaskMimeRender class, if you have python3-bottle installed you'll
# get BottleMimeRender, and so on. This relationship is not expressed
# through dependencies as it doesn't seem to the packager that such
# dependencies would actually aid in any real-world use of mimeparse;
# if you want to use it in code you've probably already picked a web
# framework, and if it's just being pulled in as a dependency of some
# other package, *that* package will express the appropriate deps on
# the web framework.
#
# Also note that *executing* mimerender.py requires the unittest or
# unittest2 module. All this does is run the test suite (as used in
# check, below). There is no Requires: for this, because it's not
# the expected use of the package, in all normal cases it will be
# used by importing the module.

%description -n python3-%{srcname}
mimerender provides a decorator that wraps a HTTP request handler to select
the correct render function for a given HTTP Accept header. It uses mimeparse
to parse the accept string and select the best available representation.
Supports Flask, Bottle, web.py and webapp2 out of the box, and it’s easy to
add support for other frameworks. This is the Python 3 build of mimerender.


%prep
%autosetup -n %{srcname}-%{version}
cp %{SOURCE1} ./LICENSE

%build
%py3_build

%install
%py3_install

%check
%{__python3} src/mimerender.py

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/%{srcname}*
%{python3_sitelib}/__pycache__/%{srcname}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.0-6
- Remove dependency on unittest2 (#1789200)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Adam Williamson <awilliam@redhat.com> - 0.6.0-1
- New upstream release 0.6.0
- Drop workarounds for things fixed upstream

* Wed Oct 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-11
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.5-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Adam Williamson <awilliam@redhat.com> - 0.5.5-1
- initial package (based on skeleton from Python guidelines)
