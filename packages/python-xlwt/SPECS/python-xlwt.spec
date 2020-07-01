%global         sum Spreadsheet python library
%global         commit dcd5cf6eb7b2cfa3f61ebf7530d1f3f7a6d10551
%global         git_tag 1.1.2
%global         shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-xlwt
Version:        1.1.2
Release:        14%{?dist}
Summary:        %{sum}

                # Utils.py is LPGL2.0+
License:        LGPLv2+ and BSD and BSD with advertising
URL:            http://pypi.python.org/pypi/xlwt
                # See also https://github.com/python-excel/xlwt
Source0:        https://github.com/python-excel/xlwt/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch
                # From upstream.
Patch0:         0001-Avoid-bad-locale-usage-upstream-263.patch

BuildRequires:  python3-devel


%description
A library for generating spreadsheet files that are compatible with
Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has
full support for Unicode. Excel spreadsheets can be generated on any
platform without needing Excel or a COM server. The only requirement
is Python 2.3 to 2.7.


%package -n python3-xlwt
Summary:      %{sum}
              # https://github.com/python-excel/xlwt/issues/73
Provides:     bundled(antlr) = 2.7.7
%{?python_provide:%python_provide python3-xlwt}

%description -n python3-xlwt
A library for generating spreadsheet files that are compatible with
Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has
full support for Unicode. Excel spreadsheets can be generated on any
platform without needing Excel or a COM server. The only requirement
is Python 2.3 to 2.7.


%prep
%autosetup -p1 -n xlwt-%{commit}
sed -i "s|tests/python.bmp|python.bmp|g" tests/test_bitmaps.py
sed -i '\;/usr/bin/env;d' xlwt/Formatting.py
cd examples
for file in  \
    panes2.py numbers_demo.py zoom_magnification.py image_chg_col_wid.py
do
    sed "s|\r||g" $file > $file.new && \
    touch -r $file $file.new && \
    mv $file.new $file
done


%build
%py3_build


%check
cd tests
PYTHONPATH=.. %{__python3} -m unittest discover


%install
%py3_install
mkdir tmp_docs
cp -ar examples docs tmp_docs


%files -n python3-xlwt
%license docs/licenses.rst
%doc README.rst tmp_docs/*
%{python3_sitelib}/xlwt
%{python3_sitelib}/*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-9
- Subpackage python2-xlwt has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.2-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 24 2016 Alec Leamas <leamas.alec@gmail.com> - 1.1.2-1
- New version
- Get sources from github instead of broken pypis source repos.
- Add patch from upstream to make tests run.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Alec Leamas <leamas.alec@gmail.com> - 1.0.0-2
- Add python3 subpackage

* Mon Jan 04 2016 Alec Leamas <leamas.alec@gmail.com> - 1.0.0-1
- Updating to new upstream.
- Remove upstreamed patch xlwt-fsf-address.
- Bundling antlr.py, the system one is unusable; upstream issue filed.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Alec Leamas <leamas.alec@gmail.com> - 0.7.4-1
- Rewriting license according to legal advice.
- Adding %%check

* Thu May 03 2012 Alec Leamas <leamas.alec@gmail.com> - 0.7.4-1
- Tentative rewrite of License tag (blocked on FE_LEGAL)
- Unbundle antlr
- Explicit naming of files in %%{python_sitelib}

* Thu May 03 2012 Alec Leamas <leamas.alec@gmail.com> - 0.7.4-1
- Fixing bad License:
- Fixing license file encoding.

* Wed May 02 2012 Alec Leamas <leamas.alec@gmail.com> - 0.7.4-1
- Initial release
