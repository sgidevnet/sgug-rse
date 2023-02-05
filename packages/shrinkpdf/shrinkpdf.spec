Name:           shrinkpdf
Version:        0
Release:        7%{?dist}
Summary:        Simple wrapper around Ghostscript to shrink PDFs

# License is BSD (3 clause)
License:        BSD
URL:            http://www.alfredklomp.com/programming/%{name}
# script is embedded in upstream page, simply copy+paste into text file
Source0:        %{url}/%{name}.sh

BuildArch:      noarch

%if 0%{?fedora} > 27
Requires:       ghostscript
%else
Requires:       ghostscript-core
%endif
Requires:       coreutils

%description
A simple wrapper around Ghostscript to shrink PDFs (as in reduce
file size) under Linux. The script feeds a PDF through Ghostscript,
which performs lossy recompression by such methods as downsampling
the images to 72 DPI. The result should be (but not always is) a much
smaller file.


%prep

%build

%install
install -p -m0755 %SOURCE0 -D %{buildroot}%{_bindir}/%{name}


%files
%{_bindir}/%{name}


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 0-5
- Requires: ghostscript (f28+) (#1536575)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 13 2016 Raphael Groner <projects.rg@smart.ms> - 0-1
- initial
