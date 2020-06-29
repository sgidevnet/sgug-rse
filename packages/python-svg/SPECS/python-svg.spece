Name:           python-svg
Version:        0.2.2b
Release:        24%{?dist}
Summary:        Python wrapper for svg

License:        BSD
URL:            http://code.google.com/p/pysvg/
Source0:        http://pysvg.googlecode.com/files/pysvg-0.2.2b.zip
Patch0:         pysvg-python3.patch

BuildArch:      noarch
BuildRequires:  python3-devel,python3-setuptools

%global _description\
pySVG is a pure Python library to create/load and manipulate SVG documents.\
\
Its main use is to "code" svg images.

%description %_description

%package -n python3-svg
Summary: %summary
%{?python_provide:%python_provide python3-svg}

%description -n python3-svg %_description

%package doc
Summary: Documentation for python-syg
Requires: python3-svg = %{version}-%{release}

%description doc %_description

These are the documentation files.

%prep
%setup -qn pysvg-%{version}

%patch0 -p1 -b .python3

rm -f doc/html/.buildinfo

# Convert to utf-8
for file in `find . -name '*.py'`; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

#Strip bad EOL encodings
for file in `find . -name '*.txt'` doc/html/_static/pygments.css; do
 sed -i "s|\r||g" $file
done
for file in `find . -name '*.py'`; do
 sed -i "s|\r||g" $file
done

#Remove shabangs.
for lib in `find . -name '*.py'`; do
 sed -i '/\/usr\/bin\/python/d' $lib
done

%build
%py3_build


%install
%py3_install

find $RPM_BUILD_ROOT -name '*.egg-info' | xargs rm -rf

%check
%{__python3} setup.py test

%files doc
%doc doc/

%files -n python3-svg
%doc doc/license.txt
%{python3_sitelib}/pysvg


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2b-24
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2b-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2b-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2b-21
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.2.2b-20
- Drop Python 2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2b-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2b-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.2b-16
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.2b-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.2b-13
- Python 2 binary package renamed to python2-svg
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.2b-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2b-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 15 2016 Jon Ciesla <limburgher@gmail.com> - 0.2.2b-8
- Add python3 support.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Jon Ciesla <limburgher@gmail.com> - 0.2.2b-2
- Remove egg-info, fix EOL encoding, add doc subpackage.

* Thu Nov 15 2012 Jon Ciesla <limburgher@gmail.com> - 0.2.2b-1
- New version with clarified license.

* Thu Jun 07 2012 Jon Ciesla <limburgher@gmail.com> - 0.2.1-1
- Initial package version

