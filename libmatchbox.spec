%define major 	1
%define libname %mklibname mb %major
%define develname %mklibname -d mb

Summary: 	Libraries for the Matchbox Desktop
Name: 		libmatchbox
Version: 	1.9
Release: 	11
URL: 		http://matchbox-project.org
License: 	LGPLv2+
Group: 		System/Libraries
Source0:	http://matchbox-project.org/sources/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch:		libmatchbox-1.9-libpng-1.5.patch
Patch1:		libmatchbox-1.9-linkage.patch
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxft-devel
BuildRequires:	pkgconfig(pango) pkgconfig(pangoxft)
BuildRequires:	png-devel
BuildRequires:	jpeg-devel
BuildRequires:	Xsettings-client-devel

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Inter-toolkit configuration settings

%description -n %{libname}
Libraries for the Matchbox Desktop.

%package -n %{develname}
Group:          Development/C
Summary:        Static libraries and header files from %{name}
Provides:	matchbox-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	libmb-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}
Obsoletes:	%mklibname -d mb 1

%description -n %{develname}
Static libraries and header files from %{name}

%prep
%setup -q
%patch -p1 -b .libpng15~
%patch1 -p1 -b .linkage~

%build
%configure2_5x --enable-xsettings --enable-png --enable-jpeg --enable-pango
%make CFLAGS="%optflags `pkg-config --cflags pango pangoxft`"

%install
%makeinstall_std
rm -rf %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/libmb/*.h
